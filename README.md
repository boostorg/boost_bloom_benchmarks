# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.46</td>
    <td align="right">4.56</td>
    <td align="right">3.66</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.10</td>
    <td align="right">10.91</td>
    <td align="right">16.75</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.03</td>
    <td align="right">4.38</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.90</td>
    <td align="right">5.10</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.65</td>
    <td align="right">15.78</td>
    <td align="right">17.72</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.85</td>
    <td align="right">4.97</td>
    <td align="right">5.03</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.45</td>
    <td align="right">5.53</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.02</td>
    <td align="right">18.83</td>
    <td align="right">16.54</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.44</td>
    <td align="right">5.33</td>
    <td align="right">5.33</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.26</td>
    <td align="right">6.37</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.03</td>
    <td align="right">23.00</td>
    <td align="right">16.83</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.21</td>
    <td align="right">5.93</td>
    <td align="right">5.95</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.76</td>
    <td align="right">6.62</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.09</td>
    <td align="right">5.76</td>
    <td align="right">5.77</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.26</td>
    <td align="right">6.59</td>
    <td align="right">6.53</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.97</td>
    <td align="right">3.27</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.51</td>
    <td align="right">8.87</td>
    <td align="right">8.86</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.16</td>
    <td align="right">9.86</td>
    <td align="right">9.86</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.49</td>
    <td align="right">3.11</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.28</td>
    <td align="right">13.25</td>
    <td align="right">13.25</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.97</td>
    <td align="right">15.03</td>
    <td align="right">15.01</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.71</td>
    <td align="right">5.76</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.01</td>
    <td align="right">14.98</td>
    <td align="right">14.93</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.17</td>
    <td align="right">16.28</td>
    <td align="right">16.45</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.82</td>
    <td align="right">5.93</td>
    <td align="right">3.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.96</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.40</td>
    <td align="right">5.11</td>
    <td align="right">5.04</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.54</td>
    <td align="right">4.98</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.06</td>
    <td align="right">3.32</td>
    <td align="right">3.32</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.20</td>
    <td align="right">4.47</td>
    <td align="right">4.46</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.43</td>
    <td align="right">5.13</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.44</td>
    <td align="right">5.51</td>
    <td align="right">3.82</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.11</td>
    <td align="right">7.74</td>
    <td align="right">5.93</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.86</td>
    <td align="right">7.61</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.49</td>
    <td align="right">5.58</td>
    <td align="right">3.80</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.00</td>
    <td align="right">9.06</td>
    <td align="right">5.94</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.32</td>
    <td align="right">9.07</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.89</td>
    <td align="right">7.01</td>
    <td align="right">13.57</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.46</td>
    <td align="right">8.98</td>
    <td align="right">17.42</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.80</td>
    <td align="right">11.13</td>
    <td align="right">11.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.34</td>
    <td align="right">8.17</td>
    <td align="right">12.48</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.21</td>
    <td align="right">9.53</td>
    <td align="right">14.33</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.38</td>
    <td align="right">15.45</td>
    <td align="right">15.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.01</td>
    <td align="right">10.39</td>
    <td align="right">12.08</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.42</td>
    <td align="right">12.68</td>
    <td align="right">15.31</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.45</td>
    <td align="right">17.02</td>
    <td align="right">16.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.46</td>
    <td align="right">12.75</td>
    <td align="right">13.21</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.84</td>
    <td align="right">14.19</td>
    <td align="right">14.95</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">22.28</td>
    <td align="right">22.95</td>
    <td align="right">23.03</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.36</td>
    <td align="right">17.34</td>
    <td align="right">7.04</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.29</td>
    <td align="right">13.17</td>
    <td align="right">17.96</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.84</td>
    <td align="right">5.15</td>
    <td align="right">5.21</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.85</td>
    <td align="right">6.07</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">20.43</td>
    <td align="right">18.93</td>
    <td align="right">18.52</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.47</td>
    <td align="right">5.61</td>
    <td align="right">5.67</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.10</td>
    <td align="right">6.16</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.39</td>
    <td align="right">25.55</td>
    <td align="right">17.91</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.67</td>
    <td align="right">6.59</td>
    <td align="right">6.36</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.82</td>
    <td align="right">7.86</td>
    <td align="right">7.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">44.42</td>
    <td align="right">40.46</td>
    <td align="right">19.06</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.28</td>
    <td align="right">8.81</td>
    <td align="right">8.94</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.80</td>
    <td align="right">9.58</td>
    <td align="right">9.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.86</td>
    <td align="right">6.69</td>
    <td align="right">6.70</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.33</td>
    <td align="right">8.02</td>
    <td align="right">7.95</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.48</td>
    <td align="right">3.93</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.50</td>
    <td align="right">10.10</td>
    <td align="right">10.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.20</td>
    <td align="right">11.27</td>
    <td align="right">11.13</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.95</td>
    <td align="right">3.86</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.15</td>
    <td align="right">15.16</td>
    <td align="right">14.76</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.00</td>
    <td align="right">16.40</td>
    <td align="right">15.08</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.11</td>
    <td align="right">7.26</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.20</td>
    <td align="right">18.45</td>
    <td align="right">17.90</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.26</td>
    <td align="right">20.88</td>
    <td align="right">21.15</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.63</td>
    <td align="right">9.52</td>
    <td align="right">6.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.61</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.28</td>
    <td align="right">6.21</td>
    <td align="right">6.12</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.41</td>
    <td align="right">6.06</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.54</td>
    <td align="right">4.03</td>
    <td align="right">4.08</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.77</td>
    <td align="right">5.26</td>
    <td align="right">5.23</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.07</td>
    <td align="right">5.96</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.49</td>
    <td align="right">7.27</td>
    <td align="right">5.05</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.84</td>
    <td align="right">9.85</td>
    <td align="right">8.88</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.82</td>
    <td align="right">9.94</td>
    <td align="right">7.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">8.90</td>
    <td align="right">10.52</td>
    <td align="right">6.64</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">14.75</td>
    <td align="right">16.03</td>
    <td align="right">10.29</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.98</td>
    <td align="right">14.09</td>
    <td align="right">9.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.27</td>
    <td align="right">8.36</td>
    <td align="right">14.22</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.82</td>
    <td align="right">10.39</td>
    <td align="right">18.26</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">13.65</td>
    <td align="right">13.97</td>
    <td align="right">13.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.48</td>
    <td align="right">9.12</td>
    <td align="right">12.86</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.52</td>
    <td align="right">10.73</td>
    <td align="right">14.80</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">18.25</td>
    <td align="right">17.98</td>
    <td align="right">18.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.11</td>
    <td align="right">12.43</td>
    <td align="right">13.04</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">18.77</td>
    <td align="right">15.45</td>
    <td align="right">16.38</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">21.09</td>
    <td align="right">21.42</td>
    <td align="right">21.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.00</td>
    <td align="right">19.69</td>
    <td align="right">15.92</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">28.28</td>
    <td align="right">22.83</td>
    <td align="right">17.83</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">33.43</td>
    <td align="right">31.60</td>
    <td align="right">31.81</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.36</td>
    <td align="right">4.28</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.64</td>
    <td align="right">8.21</td>
    <td align="right">14.76</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.11</td>
    <td align="right">3.78</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.05</td>
    <td align="right">4.44</td>
    <td align="right">4.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.49</td>
    <td align="right">12.39</td>
    <td align="right">16.04</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.49</td>
    <td align="right">4.38</td>
    <td align="right">4.37</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">7.52</td>
    <td align="right">5.12</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.65</td>
    <td align="right">15.73</td>
    <td align="right">15.07</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.03</td>
    <td align="right">4.93</td>
    <td align="right">5.10</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">8.89</td>
    <td align="right">5.92</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.03</td>
    <td align="right">20.91</td>
    <td align="right">15.67</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.26</td>
    <td align="right">5.58</td>
    <td align="right">5.77</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.77</td>
    <td align="right">3.21</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.88</td>
    <td align="right">3.38</td>
    <td align="right">3.40</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.01</td>
    <td align="right">3.33</td>
    <td align="right">3.31</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.45</td>
    <td align="right">2.37</td>
    <td align="right">2.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.54</td>
    <td align="right">3.89</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.47</td>
    <td align="right">4.14</td>
    <td align="right">4.17</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.02</td>
    <td align="right">2.12</td>
    <td align="right">2.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.29</td>
    <td align="right">6.78</td>
    <td align="right">6.84</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.47</td>
    <td align="right">6.66</td>
    <td align="right">6.72</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.00</td>
    <td align="right">4.18</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.87</td>
    <td align="right">7.39</td>
    <td align="right">7.50</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.07</td>
    <td align="right">7.91</td>
    <td align="right">7.88</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.04</td>
    <td align="right">4.27</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.47</td>
    <td align="right">2.21</td>
    <td align="right">2.21</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.43</td>
    <td align="right">3.86</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.43</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.54</td>
    <td align="right">2.27</td>
    <td align="right">2.27</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.73</td>
    <td align="right">3.52</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.60</td>
    <td align="right">3.75</td>
    <td align="right">3.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.03</td>
    <td align="right">4.13</td>
    <td align="right">2.80</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.47</td>
    <td align="right">5.83</td>
    <td align="right">4.59</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.61</td>
    <td align="right">5.81</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.13</td>
    <td align="right">4.20</td>
    <td align="right">2.86</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.24</td>
    <td align="right">6.76</td>
    <td align="right">5.02</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.55</td>
    <td align="right">6.89</td>
    <td align="right">4.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.52</td>
    <td align="right">5.72</td>
    <td align="right">11.81</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.23</td>
    <td align="right">7.59</td>
    <td align="right">16.03</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.17</td>
    <td align="right">10.41</td>
    <td align="right">10.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.88</td>
    <td align="right">7.60</td>
    <td align="right">11.85</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.42</td>
    <td align="right">9.13</td>
    <td align="right">13.66</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">16.18</td>
    <td align="right">16.28</td>
    <td align="right">16.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.23</td>
    <td align="right">9.51</td>
    <td align="right">11.56</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.53</td>
    <td align="right">11.95</td>
    <td align="right">14.48</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">19.09</td>
    <td align="right">19.27</td>
    <td align="right">19.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.40</td>
    <td align="right">11.79</td>
    <td align="right">12.42</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.47</td>
    <td align="right">13.63</td>
    <td align="right">14.12</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">26.64</td>
    <td align="right">26.15</td>
    <td align="right">25.42</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.18</td>
    <td align="right">16.91</td>
    <td align="right">8.59</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.55</td>
    <td align="right">11.23</td>
    <td align="right">16.64</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.64</td>
    <td align="right">4.64</td>
    <td align="right">4.72</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.07</td>
    <td align="right">5.50</td>
    <td align="right">5.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.55</td>
    <td align="right">15.92</td>
    <td align="right">17.50</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.76</td>
    <td align="right">5.14</td>
    <td align="right">5.18</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.32</td>
    <td align="right">5.94</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">41.01</td>
    <td align="right">47.74</td>
    <td align="right">20.25</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.61</td>
    <td align="right">9.35</td>
    <td align="right">9.18</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.71</td>
    <td align="right">9.77</td>
    <td align="right">8.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">37.21</td>
    <td align="right">37.81</td>
    <td align="right">18.22</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">17.30</td>
    <td align="right">15.81</td>
    <td align="right">15.15</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.34</td>
    <td align="right">10.71</td>
    <td align="right">10.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.71</td>
    <td align="right">4.31</td>
    <td align="right">4.32</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.83</td>
    <td align="right">4.36</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.14</td>
    <td align="right">3.18</td>
    <td align="right">3.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.28</td>
    <td align="right">5.09</td>
    <td align="right">4.80</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.25</td>
    <td align="right">5.12</td>
    <td align="right">5.14</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.56</td>
    <td align="right">2.73</td>
    <td align="right">2.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">7.09</td>
    <td align="right">10.86</td>
    <td align="right">12.21</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.41</td>
    <td align="right">9.79</td>
    <td align="right">9.23</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.97</td>
    <td align="right">8.51</td>
    <td align="right">7.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">13.17</td>
    <td align="right">17.79</td>
    <td align="right">17.23</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.49</td>
    <td align="right">12.50</td>
    <td align="right">11.84</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.09</td>
    <td align="right">7.25</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.13</td>
    <td align="right">2.98</td>
    <td align="right">2.96</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.33</td>
    <td align="right">4.87</td>
    <td align="right">4.89</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.40</td>
    <td align="right">4.76</td>
    <td align="right">4.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.08</td>
    <td align="right">2.97</td>
    <td align="right">2.93</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.43</td>
    <td align="right">4.29</td>
    <td align="right">4.31</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.37</td>
    <td align="right">4.77</td>
    <td align="right">5.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.68</td>
    <td align="right">5.52</td>
    <td align="right">4.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.94</td>
    <td align="right">9.46</td>
    <td align="right">7.39</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.58</td>
    <td align="right">10.55</td>
    <td align="right">8.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">12.63</td>
    <td align="right">14.55</td>
    <td align="right">10.04</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.17</td>
    <td align="right">10.50</td>
    <td align="right">6.91</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.06</td>
    <td align="right">11.25</td>
    <td align="right">6.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.14</td>
    <td align="right">7.17</td>
    <td align="right">12.74</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.06</td>
    <td align="right">9.30</td>
    <td align="right">17.07</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">13.92</td>
    <td align="right">14.29</td>
    <td align="right">14.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.92</td>
    <td align="right">9.74</td>
    <td align="right">13.22</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">19.34</td>
    <td align="right">13.64</td>
    <td align="right">14.91</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">18.26</td>
    <td align="right">18.40</td>
    <td align="right">18.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.94</td>
    <td align="right">12.11</td>
    <td align="right">12.84</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">18.14</td>
    <td align="right">14.91</td>
    <td align="right">16.08</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">24.41</td>
    <td align="right">24.89</td>
    <td align="right">25.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">24.65</td>
    <td align="right">16.93</td>
    <td align="right">14.49</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">23.59</td>
    <td align="right">21.88</td>
    <td align="right">19.34</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">40.64</td>
    <td align="right">44.00</td>
    <td align="right">47.68</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">21.03</td>
    <td align="right">4.38</td>
    <td align="right">3.43</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.32</td>
    <td align="right">4.77</td>
    <td align="right">12.42</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.44</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.73</td>
    <td align="right">1.42</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.57</td>
    <td align="right">7.56</td>
    <td align="right">12.91</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.53</td>
    <td align="right">1.50</td>
    <td align="right">1.44</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.78</td>
    <td align="right">1.51</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.04</td>
    <td align="right">8.31</td>
    <td align="right">11.01</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.53</td>
    <td align="right">2.37</td>
    <td align="right">2.39</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.80</td>
    <td align="right">1.77</td>
    <td align="right">1.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.86</td>
    <td align="right">12.69</td>
    <td align="right">12.07</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.75</td>
    <td align="right">1.97</td>
    <td align="right">2.16</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.94</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.45</td>
    <td align="right">1.81</td>
    <td align="right">1.79</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.51</td>
    <td align="right">1.93</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.16</td>
    <td align="right">1.85</td>
    <td align="right">1.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.40</td>
    <td align="right">2.17</td>
    <td align="right">2.16</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.03</td>
    <td align="right">2.41</td>
    <td align="right">2.46</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.69</td>
    <td align="right">1.51</td>
    <td align="right">1.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.50</td>
    <td align="right">3.10</td>
    <td align="right">4.45</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.49</td>
    <td align="right">3.19</td>
    <td align="right">3.31</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.32</td>
    <td align="right">2.68</td>
    <td align="right">1.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.11</td>
    <td align="right">3.70</td>
    <td align="right">3.73</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.27</td>
    <td align="right">4.51</td>
    <td align="right">4.29</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.17</td>
    <td align="right">1.87</td>
    <td align="right">1.79</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.32</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.36</td>
    <td align="right">3.89</td>
    <td align="right">1.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.32</td>
    <td align="right">1.75</td>
    <td align="right">1.72</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.00</td>
    <td align="right">2.09</td>
    <td align="right">1.98</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.09</td>
    <td align="right">2.42</td>
    <td align="right">4.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.00</td>
    <td align="right">2.53</td>
    <td align="right">1.82</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.73</td>
    <td align="right">3.13</td>
    <td align="right">3.04</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.18</td>
    <td align="right">3.05</td>
    <td align="right">3.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">7.13</td>
    <td align="right">3.25</td>
    <td align="right">1.98</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.80</td>
    <td align="right">3.60</td>
    <td align="right">3.59</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.25</td>
    <td align="right">4.43</td>
    <td align="right">4.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.47</td>
    <td align="right">3.42</td>
    <td align="right">10.04</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">9.81</td>
    <td align="right">4.28</td>
    <td align="right">13.71</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">8.22</td>
    <td align="right">5.29</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">6.43</td>
    <td align="right">4.97</td>
    <td align="right">11.30</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">8.66</td>
    <td align="right">5.16</td>
    <td align="right">11.64</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">11.70</td>
    <td align="right">7.59</td>
    <td align="right">7.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.61</td>
    <td align="right">5.35</td>
    <td align="right">11.24</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">8.81</td>
    <td align="right">6.40</td>
    <td align="right">12.44</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.96</td>
    <td align="right">8.31</td>
    <td align="right">7.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">7.56</td>
    <td align="right">7.48</td>
    <td align="right">10.55</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">9.41</td>
    <td align="right">6.38</td>
    <td align="right">15.92</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">18.31</td>
    <td align="right">11.78</td>
    <td align="right">11.36</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.48</td>
    <td align="right">13.29</td>
    <td align="right">8.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.32</td>
    <td align="right">9.00</td>
    <td align="right">18.46</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.50</td>
    <td align="right">3.54</td>
    <td align="right">2.37</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.79</td>
    <td align="right">2.41</td>
    <td align="right">3.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.02</td>
    <td align="right">23.73</td>
    <td align="right">22.17</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.96</td>
    <td align="right">4.58</td>
    <td align="right">5.00</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.81</td>
    <td align="right">5.28</td>
    <td align="right">6.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">44.96</td>
    <td align="right">36.66</td>
    <td align="right">22.64</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.25</td>
    <td align="right">8.17</td>
    <td align="right">8.69</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.53</td>
    <td align="right">7.69</td>
    <td align="right">8.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">69.29</td>
    <td align="right">51.34</td>
    <td align="right">26.95</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.16</td>
    <td align="right">10.02</td>
    <td align="right">9.78</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.13</td>
    <td align="right">6.69</td>
    <td align="right">7.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.21</td>
    <td align="right">3.87</td>
    <td align="right">4.44</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.79</td>
    <td align="right">4.16</td>
    <td align="right">3.80</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.16</td>
    <td align="right">3.52</td>
    <td align="right">4.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.98</td>
    <td align="right">4.46</td>
    <td align="right">8.01</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.52</td>
    <td align="right">6.66</td>
    <td align="right">6.78</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.73</td>
    <td align="right">6.48</td>
    <td align="right">3.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">13.56</td>
    <td align="right">13.04</td>
    <td align="right">12.69</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">16.33</td>
    <td align="right">14.41</td>
    <td align="right">13.25</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.05</td>
    <td align="right">10.96</td>
    <td align="right">7.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">20.62</td>
    <td align="right">17.51</td>
    <td align="right">17.99</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.87</td>
    <td align="right">18.21</td>
    <td align="right">19.10</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">13.36</td>
    <td align="right">14.28</td>
    <td align="right">7.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.40</td>
    <td align="right">2.84</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.08</td>
    <td align="right">3.07</td>
    <td align="right">2.88</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.75</td>
    <td align="right">2.63</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.83</td>
    <td align="right">2.96</td>
    <td align="right">3.04</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.66</td>
    <td align="right">4.09</td>
    <td align="right">4.01</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.17</td>
    <td align="right">4.57</td>
    <td align="right">4.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.38</td>
    <td align="right">7.51</td>
    <td align="right">5.11</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.53</td>
    <td align="right">8.90</td>
    <td align="right">9.00</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">9.61</td>
    <td align="right">8.71</td>
    <td align="right">8.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.44</td>
    <td align="right">10.83</td>
    <td align="right">6.08</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.22</td>
    <td align="right">12.32</td>
    <td align="right">12.42</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.60</td>
    <td align="right">13.24</td>
    <td align="right">13.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">4.53</td>
    <td align="right">4.12</td>
    <td align="right">11.02</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.82</td>
    <td align="right">4.98</td>
    <td align="right">13.68</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">8.76</td>
    <td align="right">6.91</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.07</td>
    <td align="right">7.29</td>
    <td align="right">12.00</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.54</td>
    <td align="right">7.73</td>
    <td align="right">13.08</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">13.45</td>
    <td align="right">12.58</td>
    <td align="right">12.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.03</td>
    <td align="right">12.13</td>
    <td align="right">14.43</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.05</td>
    <td align="right">14.48</td>
    <td align="right">15.78</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">24.35</td>
    <td align="right">20.32</td>
    <td align="right">20.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">21.65</td>
    <td align="right">16.27</td>
    <td align="right">15.76</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">27.49</td>
    <td align="right">19.37</td>
    <td align="right">16.52</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.09</td>
    <td align="right">37.06</td>
    <td align="right">36.08</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.73</td>
    <td align="right">5.67</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.01</td>
    <td align="right">12.77</td>
    <td align="right">17.05</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.79</td>
    <td align="right">4.39</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.97</td>
    <td align="right">5.23</td>
    <td align="right">5.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.32</td>
    <td align="right">17.78</td>
    <td align="right">17.73</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.92</td>
    <td align="right">4.90</td>
    <td align="right">4.72</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.02</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.40</td>
    <td align="right">21.22</td>
    <td align="right">16.59</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.61</td>
    <td align="right">5.31</td>
    <td align="right">5.33</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.29</td>
    <td align="right">6.58</td>
    <td align="right">6.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.92</td>
    <td align="right">27.12</td>
    <td align="right">17.50</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.91</td>
    <td align="right">5.92</td>
    <td align="right">6.04</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.42</td>
    <td align="right">7.43</td>
    <td align="right">7.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.88</td>
    <td align="right">5.53</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.15</td>
    <td align="right">5.57</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.36</td>
    <td align="right">3.98</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.63</td>
    <td align="right">8.16</td>
    <td align="right">8.14</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.56</td>
    <td align="right">8.79</td>
    <td align="right">7.90</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.90</td>
    <td align="right">4.82</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">14.95</td>
    <td align="right">10.97</td>
    <td align="right">10.73</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">24.38</td>
    <td align="right">10.56</td>
    <td align="right">10.55</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.97</td>
    <td align="right">7.09</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.73</td>
    <td align="right">12.46</td>
    <td align="right">12.48</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">21.90</td>
    <td align="right">13.54</td>
    <td align="right">13.47</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.02</td>
    <td align="right">7.13</td>
    <td align="right">5.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.24</td>
    <td align="right">3.85</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.53</td>
    <td align="right">5.47</td>
    <td align="right">5.47</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.65</td>
    <td align="right">5.38</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.33</td>
    <td align="right">5.56</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.79</td>
    <td align="right">5.79</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.91</td>
    <td align="right">7.06</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.10</td>
    <td align="right">6.82</td>
    <td align="right">5.04</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.81</td>
    <td align="right">9.34</td>
    <td align="right">7.61</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.61</td>
    <td align="right">9.33</td>
    <td align="right">7.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.11</td>
    <td align="right">6.89</td>
    <td align="right">5.03</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.09</td>
    <td align="right">10.70</td>
    <td align="right">7.65</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.12</td>
    <td align="right">10.45</td>
    <td align="right">7.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.55</td>
    <td align="right">8.65</td>
    <td align="right">13.69</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.45</td>
    <td align="right">11.65</td>
    <td align="right">17.10</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.87</td>
    <td align="right">10.60</td>
    <td align="right">10.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.96</td>
    <td align="right">10.98</td>
    <td align="right">12.95</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.45</td>
    <td align="right">13.43</td>
    <td align="right">14.76</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">18.75</td>
    <td align="right">18.13</td>
    <td align="right">17.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.30</td>
    <td align="right">14.22</td>
    <td align="right">12.69</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">19.09</td>
    <td align="right">17.52</td>
    <td align="right">15.31</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">21.49</td>
    <td align="right">18.68</td>
    <td align="right">19.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.39</td>
    <td align="right">17.48</td>
    <td align="right">14.00</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">20.59</td>
    <td align="right">20.48</td>
    <td align="right">14.82</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">30.00</td>
    <td align="right">28.23</td>
    <td align="right">28.27</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.17</td>
    <td align="right">20.53</td>
    <td align="right">7.42</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.44</td>
    <td align="right">13.03</td>
    <td align="right">17.64</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.02</td>
    <td align="right">4.49</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.95</td>
    <td align="right">5.55</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.98</td>
    <td align="right">18.79</td>
    <td align="right">18.49</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.52</td>
    <td align="right">5.04</td>
    <td align="right">5.06</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.28</td>
    <td align="right">6.35</td>
    <td align="right">6.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">28.15</td>
    <td align="right">23.36</td>
    <td align="right">17.31</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.03</td>
    <td align="right">5.69</td>
    <td align="right">5.75</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.72</td>
    <td align="right">7.33</td>
    <td align="right">7.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">46.67</td>
    <td align="right">43.20</td>
    <td align="right">19.33</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.96</td>
    <td align="right">9.13</td>
    <td align="right">9.33</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.01</td>
    <td align="right">9.43</td>
    <td align="right">9.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.26</td>
    <td align="right">6.23</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">11.91</td>
    <td align="right">6.32</td>
    <td align="right">6.33</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.72</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.71</td>
    <td align="right">9.70</td>
    <td align="right">9.63</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.62</td>
    <td align="right">9.65</td>
    <td align="right">9.83</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.54</td>
    <td align="right">5.36</td>
    <td align="right">4.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.43</td>
    <td align="right">15.29</td>
    <td align="right">13.71</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">25.52</td>
    <td align="right">12.30</td>
    <td align="right">12.35</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.97</td>
    <td align="right">8.98</td>
    <td align="right">7.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">23.18</td>
    <td align="right">21.27</td>
    <td align="right">18.79</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">33.67</td>
    <td align="right">20.04</td>
    <td align="right">31.80</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.22</td>
    <td align="right">14.83</td>
    <td align="right">9.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.69</td>
    <td align="right">4.12</td>
    <td align="right">4.13</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.10</td>
    <td align="right">5.91</td>
    <td align="right">5.90</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.24</td>
    <td align="right">5.78</td>
    <td align="right">5.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.85</td>
    <td align="right">5.99</td>
    <td align="right">5.10</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.76</td>
    <td align="right">6.33</td>
    <td align="right">5.66</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">8.73</td>
    <td align="right">9.29</td>
    <td align="right">7.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.29</td>
    <td align="right">9.74</td>
    <td align="right">11.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">14.12</td>
    <td align="right">12.85</td>
    <td align="right">12.67</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">14.29</td>
    <td align="right">11.70</td>
    <td align="right">8.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">16.09</td>
    <td align="right">20.21</td>
    <td align="right">13.97</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">23.21</td>
    <td align="right">25.62</td>
    <td align="right">19.73</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">24.04</td>
    <td align="right">23.97</td>
    <td align="right">12.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">9.85</td>
    <td align="right">9.89</td>
    <td align="right">14.43</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.94</td>
    <td align="right">12.96</td>
    <td align="right">18.03</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">18.51</td>
    <td align="right">16.88</td>
    <td align="right">17.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">14.15</td>
    <td align="right">12.48</td>
    <td align="right">16.78</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">24.41</td>
    <td align="right">22.45</td>
    <td align="right">15.38</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">24.32</td>
    <td align="right">22.81</td>
    <td align="right">23.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">17.24</td>
    <td align="right">17.79</td>
    <td align="right">14.43</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.91</td>
    <td align="right">30.78</td>
    <td align="right">19.92</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">30.66</td>
    <td align="right">27.80</td>
    <td align="right">28.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">31.60</td>
    <td align="right">28.09</td>
    <td align="right">17.30</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">34.64</td>
    <td align="right">34.48</td>
    <td align="right">19.19</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">40.69</td>
    <td align="right">39.12</td>
    <td align="right">39.28</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">60.42</td>
    <td align="right">32.30</td>
    <td align="right">16.75</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.65</td>
    <td align="right">41.91</td>
    <td align="right">35.97</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.54</td>
    <td align="right">15.59</td>
    <td align="right">15.59</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.27</td>
    <td align="right">19.18</td>
    <td align="right">19.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.17</td>
    <td align="right">63.97</td>
    <td align="right">39.20</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.38</td>
    <td align="right">19.55</td>
    <td align="right">19.54</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.28</td>
    <td align="right">18.61</td>
    <td align="right">18.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.95</td>
    <td align="right">78.03</td>
    <td align="right">38.61</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.46</td>
    <td align="right">18.52</td>
    <td align="right">18.64</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.15</td>
    <td align="right">18.31</td>
    <td align="right">18.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.13</td>
    <td align="right">97.49</td>
    <td align="right">37.33</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.30</td>
    <td align="right">18.78</td>
    <td align="right">18.78</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.07</td>
    <td align="right">19.97</td>
    <td align="right">20.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.27</td>
    <td align="right">21.20</td>
    <td align="right">21.23</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.81</td>
    <td align="right">22.24</td>
    <td align="right">22.26</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.02</td>
    <td align="right">13.65</td>
    <td align="right">13.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.45</td>
    <td align="right">26.09</td>
    <td align="right">26.06</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.94</td>
    <td align="right">27.90</td>
    <td align="right">27.86</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.14</td>
    <td align="right">16.32</td>
    <td align="right">15.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.09</td>
    <td align="right">33.10</td>
    <td align="right">33.10</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.36</td>
    <td align="right">46.74</td>
    <td align="right">46.97</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.04</td>
    <td align="right">19.60</td>
    <td align="right">19.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.63</td>
    <td align="right">36.21</td>
    <td align="right">36.20</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.88</td>
    <td align="right">56.53</td>
    <td align="right">56.56</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">22.76</td>
    <td align="right">25.57</td>
    <td align="right">25.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.41</td>
    <td align="right">15.61</td>
    <td align="right">15.64</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.30</td>
    <td align="right">21.29</td>
    <td align="right">21.24</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.79</td>
    <td align="right">22.24</td>
    <td align="right">22.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.92</td>
    <td align="right">20.47</td>
    <td align="right">20.44</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.46</td>
    <td align="right">26.10</td>
    <td align="right">26.12</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.90</td>
    <td align="right">27.85</td>
    <td align="right">27.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.58</td>
    <td align="right">24.83</td>
    <td align="right">24.81</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.13</td>
    <td align="right">33.05</td>
    <td align="right">33.06</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.25</td>
    <td align="right">46.67</td>
    <td align="right">47.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.56</td>
    <td align="right">37.40</td>
    <td align="right">37.47</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.63</td>
    <td align="right">36.22</td>
    <td align="right">36.25</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.91</td>
    <td align="right">56.60</td>
    <td align="right">56.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.26</td>
    <td align="right">20.82</td>
    <td align="right">25.51</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.39</td>
    <td align="right">29.18</td>
    <td align="right">34.63</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.87</td>
    <td align="right">30.22</td>
    <td align="right">30.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.19</td>
    <td align="right">28.31</td>
    <td align="right">26.29</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">39.12</td>
    <td align="right">33.50</td>
    <td align="right">30.55</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">38.23</td>
    <td align="right">38.69</td>
    <td align="right">39.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.72</td>
    <td align="right">33.85</td>
    <td align="right">25.69</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">47.06</td>
    <td align="right">41.89</td>
    <td align="right">33.40</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.84</td>
    <td align="right">41.45</td>
    <td align="right">41.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.72</td>
    <td align="right">40.25</td>
    <td align="right">26.87</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">49.27</td>
    <td align="right">44.02</td>
    <td align="right">31.36</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">55.34</td>
    <td align="right">59.17</td>
    <td align="right">59.23</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">71.67</td>
    <td align="right">105.72</td>
    <td align="right">20.62</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.53</td>
    <td align="right">42.58</td>
    <td align="right">38.77</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.73</td>
    <td align="right">15.51</td>
    <td align="right">15.51</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.35</td>
    <td align="right">19.20</td>
    <td align="right">19.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.24</td>
    <td align="right">61.91</td>
    <td align="right">40.19</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.32</td>
    <td align="right">19.82</td>
    <td align="right">19.90</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.04</td>
    <td align="right">18.74</td>
    <td align="right">18.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">43.42</td>
    <td align="right">75.83</td>
    <td align="right">38.70</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.22</td>
    <td align="right">18.65</td>
    <td align="right">18.91</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">17.98</td>
    <td align="right">18.51</td>
    <td align="right">18.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">58.75</td>
    <td align="right">97.00</td>
    <td align="right">38.90</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">20.06</td>
    <td align="right">21.38</td>
    <td align="right">20.86</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">21.21</td>
    <td align="right">22.31</td>
    <td align="right">22.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.40</td>
    <td align="right">21.66</td>
    <td align="right">21.63</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.62</td>
    <td align="right">22.72</td>
    <td align="right">22.72</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.03</td>
    <td align="right">13.88</td>
    <td align="right">13.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.39</td>
    <td align="right">25.30</td>
    <td align="right">25.45</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.49</td>
    <td align="right">28.06</td>
    <td align="right">28.04</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.57</td>
    <td align="right">16.03</td>
    <td align="right">15.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.13</td>
    <td align="right">34.84</td>
    <td align="right">34.32</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.56</td>
    <td align="right">47.87</td>
    <td align="right">48.95</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.93</td>
    <td align="right">19.22</td>
    <td align="right">19.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">38.05</td>
    <td align="right">40.56</td>
    <td align="right">44.41</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.39</td>
    <td align="right">59.48</td>
    <td align="right">59.00</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">28.36</td>
    <td align="right">29.00</td>
    <td align="right">31.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.58</td>
    <td align="right">15.76</td>
    <td align="right">15.82</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.44</td>
    <td align="right">21.69</td>
    <td align="right">21.64</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.61</td>
    <td align="right">22.69</td>
    <td align="right">22.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.70</td>
    <td align="right">20.30</td>
    <td align="right">20.20</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.50</td>
    <td align="right">25.63</td>
    <td align="right">25.66</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.32</td>
    <td align="right">28.40</td>
    <td align="right">28.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">28.49</td>
    <td align="right">24.91</td>
    <td align="right">25.08</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.47</td>
    <td align="right">34.03</td>
    <td align="right">34.25</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">66.10</td>
    <td align="right">48.47</td>
    <td align="right">49.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">45.05</td>
    <td align="right">46.70</td>
    <td align="right">44.90</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">36.32</td>
    <td align="right">40.12</td>
    <td align="right">40.19</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">83.72</td>
    <td align="right">60.78</td>
    <td align="right">60.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.51</td>
    <td align="right">21.28</td>
    <td align="right">25.96</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">31.87</td>
    <td align="right">29.31</td>
    <td align="right">35.83</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.13</td>
    <td align="right">32.22</td>
    <td align="right">32.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">27.02</td>
    <td align="right">28.26</td>
    <td align="right">26.26</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">42.31</td>
    <td align="right">35.99</td>
    <td align="right">31.94</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">39.17</td>
    <td align="right">40.19</td>
    <td align="right">40.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">34.52</td>
    <td align="right">34.94</td>
    <td align="right">25.66</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">51.65</td>
    <td align="right">45.41</td>
    <td align="right">34.67</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">41.09</td>
    <td align="right">42.47</td>
    <td align="right">42.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.13</td>
    <td align="right">45.79</td>
    <td align="right">28.96</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">61.35</td>
    <td align="right">56.78</td>
    <td align="right">37.91</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">57.07</td>
    <td align="right">62.68</td>
    <td align="right">62.47</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.98</td>
    <td align="right">10.06</td>
    <td align="right">6.87</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.66</td>
    <td align="right">22.60</td>
    <td align="right">26.55</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.27</td>
    <td align="right">12.33</td>
    <td align="right">12.30</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.72</td>
    <td align="right">13.85</td>
    <td align="right">13.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.42</td>
    <td align="right">35.14</td>
    <td align="right">29.08</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.14</td>
    <td align="right">14.06</td>
    <td align="right">14.06</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.64</td>
    <td align="right">15.27</td>
    <td align="right">15.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.71</td>
    <td align="right">47.01</td>
    <td align="right">29.31</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.73</td>
    <td align="right">15.38</td>
    <td align="right">15.33</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.27</td>
    <td align="right">16.83</td>
    <td align="right">16.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">30.87</td>
    <td align="right">59.98</td>
    <td align="right">30.96</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">16.12</td>
    <td align="right">16.23</td>
    <td align="right">16.21</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">17.22</td>
    <td align="right">17.76</td>
    <td align="right">17.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.67</td>
    <td align="right">15.98</td>
    <td align="right">16.00</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.19</td>
    <td align="right">16.57</td>
    <td align="right">16.65</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">6.98</td>
    <td align="right">9.32</td>
    <td align="right">9.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.29</td>
    <td align="right">22.38</td>
    <td align="right">22.41</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.69</td>
    <td align="right">22.33</td>
    <td align="right">22.37</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.85</td>
    <td align="right">14.05</td>
    <td align="right">13.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.01</td>
    <td align="right">31.91</td>
    <td align="right">32.07</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.49</td>
    <td align="right">30.81</td>
    <td align="right">30.65</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.24</td>
    <td align="right">17.52</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.15</td>
    <td align="right">35.60</td>
    <td align="right">35.59</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.14</td>
    <td align="right">35.67</td>
    <td align="right">35.64</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.30</td>
    <td align="right">20.53</td>
    <td align="right">20.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.53</td>
    <td align="right">9.34</td>
    <td align="right">9.32</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.68</td>
    <td align="right">16.02</td>
    <td align="right">16.01</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.21</td>
    <td align="right">16.63</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.70</td>
    <td align="right">13.66</td>
    <td align="right">13.67</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.28</td>
    <td align="right">22.37</td>
    <td align="right">22.39</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.67</td>
    <td align="right">22.32</td>
    <td align="right">22.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.57</td>
    <td align="right">17.56</td>
    <td align="right">17.60</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.02</td>
    <td align="right">32.01</td>
    <td align="right">31.96</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.51</td>
    <td align="right">30.67</td>
    <td align="right">30.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.00</td>
    <td align="right">20.96</td>
    <td align="right">20.87</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.99</td>
    <td align="right">35.55</td>
    <td align="right">35.55</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.08</td>
    <td align="right">35.61</td>
    <td align="right">35.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.76</td>
    <td align="right">16.11</td>
    <td align="right">19.89</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.57</td>
    <td align="right">33.34</td>
    <td align="right">36.83</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.44</td>
    <td align="right">23.92</td>
    <td align="right">23.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.62</td>
    <td align="right">23.25</td>
    <td align="right">20.58</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.02</td>
    <td align="right">37.68</td>
    <td align="right">35.85</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.45</td>
    <td align="right">31.67</td>
    <td align="right">31.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">23.86</td>
    <td align="right">29.74</td>
    <td align="right">20.44</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.52</td>
    <td align="right">45.61</td>
    <td align="right">37.84</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">29.83</td>
    <td align="right">34.74</td>
    <td align="right">34.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">29.80</td>
    <td align="right">35.37</td>
    <td align="right">21.28</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">66.39</td>
    <td align="right">47.23</td>
    <td align="right">37.25</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">42.13</td>
    <td align="right">45.89</td>
    <td align="right">45.78</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.61</td>
    <td align="right">48.43</td>
    <td align="right">10.57</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.09</td>
    <td align="right">22.66</td>
    <td align="right">28.14</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">10.54</td>
    <td align="right">12.49</td>
    <td align="right">12.46</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.34</td>
    <td align="right">13.96</td>
    <td align="right">14.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.65</td>
    <td align="right">34.83</td>
    <td align="right">30.65</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.65</td>
    <td align="right">13.88</td>
    <td align="right">14.34</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">15.62</td>
    <td align="right">15.19</td>
    <td align="right">14.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">26.51</td>
    <td align="right">47.06</td>
    <td align="right">30.05</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">19.67</td>
    <td align="right">15.77</td>
    <td align="right">15.03</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">18.54</td>
    <td align="right">16.17</td>
    <td align="right">16.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">30.02</td>
    <td align="right">59.97</td>
    <td align="right">30.63</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">15.81</td>
    <td align="right">15.71</td>
    <td align="right">15.77</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">16.80</td>
    <td align="right">17.37</td>
    <td align="right">17.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.01</td>
    <td align="right">16.49</td>
    <td align="right">16.54</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.27</td>
    <td align="right">17.29</td>
    <td align="right">17.33</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.15</td>
    <td align="right">9.36</td>
    <td align="right">9.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.84</td>
    <td align="right">21.95</td>
    <td align="right">22.09</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.86</td>
    <td align="right">21.94</td>
    <td align="right">21.93</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.18</td>
    <td align="right">14.07</td>
    <td align="right">13.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.80</td>
    <td align="right">32.65</td>
    <td align="right">32.65</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.46</td>
    <td align="right">31.00</td>
    <td align="right">31.06</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.00</td>
    <td align="right">16.79</td>
    <td align="right">16.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">26.42</td>
    <td align="right">36.41</td>
    <td align="right">36.15</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">32.82</td>
    <td align="right">35.04</td>
    <td align="right">34.93</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">15.70</td>
    <td align="right">19.58</td>
    <td align="right">19.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.65</td>
    <td align="right">9.45</td>
    <td align="right">9.46</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.07</td>
    <td align="right">16.50</td>
    <td align="right">16.49</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.26</td>
    <td align="right">17.35</td>
    <td align="right">17.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.43</td>
    <td align="right">13.39</td>
    <td align="right">13.36</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.89</td>
    <td align="right">21.96</td>
    <td align="right">22.12</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.87</td>
    <td align="right">21.95</td>
    <td align="right">21.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">12.64</td>
    <td align="right">16.84</td>
    <td align="right">16.81</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.74</td>
    <td align="right">32.62</td>
    <td align="right">32.60</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.47</td>
    <td align="right">31.02</td>
    <td align="right">30.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">15.78</td>
    <td align="right">20.20</td>
    <td align="right">19.93</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">26.55</td>
    <td align="right">36.08</td>
    <td align="right">36.20</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">32.87</td>
    <td align="right">35.20</td>
    <td align="right">35.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.39</td>
    <td align="right">16.39</td>
    <td align="right">20.15</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">48.84</td>
    <td align="right">33.62</td>
    <td align="right">36.55</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">21.59</td>
    <td align="right">25.88</td>
    <td align="right">25.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">19.81</td>
    <td align="right">23.11</td>
    <td align="right">20.55</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">54.22</td>
    <td align="right">36.92</td>
    <td align="right">34.53</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">29.09</td>
    <td align="right">33.23</td>
    <td align="right">33.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">23.52</td>
    <td align="right">29.61</td>
    <td align="right">20.27</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">59.84</td>
    <td align="right">45.46</td>
    <td align="right">37.38</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">31.63</td>
    <td align="right">35.88</td>
    <td align="right">35.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">29.33</td>
    <td align="right">35.44</td>
    <td align="right">21.36</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">64.97</td>
    <td align="right">47.67</td>
    <td align="right">37.53</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">43.00</td>
    <td align="right">46.61</td>
    <td align="right">46.73</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">43.41</td>
    <td align="right">8.79</td>
    <td align="right">6.66</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.78</td>
    <td align="right">54.91</td>
    <td align="right">41.62</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.14</td>
    <td align="right">19.71</td>
    <td align="right">23.40</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">23.16</td>
    <td align="right">21.62</td>
    <td align="right">24.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">91.42</td>
    <td align="right">81.30</td>
    <td align="right">44.27</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.38</td>
    <td align="right">21.32</td>
    <td align="right">23.87</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.33</td>
    <td align="right">22.79</td>
    <td align="right">24.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">111.25</td>
    <td align="right">102.58</td>
    <td align="right">45.06</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.45</td>
    <td align="right">22.83</td>
    <td align="right">24.51</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">28.24</td>
    <td align="right">24.53</td>
    <td align="right">25.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">143.34</td>
    <td align="right">127.40</td>
    <td align="right">45.81</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.21</td>
    <td align="right">24.43</td>
    <td align="right">26.04</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.20</td>
    <td align="right">25.60</td>
    <td align="right">26.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.18</td>
    <td align="right">41.47</td>
    <td align="right">41.52</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">29.16</td>
    <td align="right">41.84</td>
    <td align="right">41.55</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">19.08</td>
    <td align="right">26.02</td>
    <td align="right">26.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.25</td>
    <td align="right">56.46</td>
    <td align="right">56.91</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.93</td>
    <td align="right">57.93</td>
    <td align="right">58.12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.85</td>
    <td align="right">36.83</td>
    <td align="right">26.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">41.05</td>
    <td align="right">77.02</td>
    <td align="right">76.81</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.60</td>
    <td align="right">78.21</td>
    <td align="right">78.23</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.60</td>
    <td align="right">55.56</td>
    <td align="right">40.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.20</td>
    <td align="right">86.37</td>
    <td align="right">86.31</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">50.59</td>
    <td align="right">93.26</td>
    <td align="right">93.05</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.85</td>
    <td align="right">56.41</td>
    <td align="right">40.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.90</td>
    <td align="right">26.60</td>
    <td align="right">26.62</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">21.00</td>
    <td align="right">29.71</td>
    <td align="right">29.68</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">21.09</td>
    <td align="right">31.38</td>
    <td align="right">31.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.21</td>
    <td align="right">46.76</td>
    <td align="right">35.43</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.82</td>
    <td align="right">40.39</td>
    <td align="right">27.94</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.14</td>
    <td align="right">52.24</td>
    <td align="right">40.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.95</td>
    <td align="right">54.70</td>
    <td align="right">38.93</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.43</td>
    <td align="right">53.21</td>
    <td align="right">35.48</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.47</td>
    <td align="right">61.61</td>
    <td align="right">44.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">29.07</td>
    <td align="right">55.87</td>
    <td align="right">39.76</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.61</td>
    <td align="right">64.89</td>
    <td align="right">44.82</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.66</td>
    <td align="right">64.75</td>
    <td align="right">45.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.23</td>
    <td align="right">42.87</td>
    <td align="right">35.23</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.88</td>
    <td align="right">53.82</td>
    <td align="right">40.53</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">37.43</td>
    <td align="right">59.93</td>
    <td align="right">60.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.66</td>
    <td align="right">60.35</td>
    <td align="right">35.55</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.84</td>
    <td align="right">61.30</td>
    <td align="right">38.48</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">45.41</td>
    <td align="right">77.72</td>
    <td align="right">77.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">42.71</td>
    <td align="right">75.19</td>
    <td align="right">36.01</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">49.95</td>
    <td align="right">79.92</td>
    <td align="right">40.10</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.68</td>
    <td align="right">83.41</td>
    <td align="right">83.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">53.42</td>
    <td align="right">94.43</td>
    <td align="right">37.52</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">58.46</td>
    <td align="right">96.14</td>
    <td align="right">39.96</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">67.73</td>
    <td align="right">118.89</td>
    <td align="right">118.34</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">71.89</td>
    <td align="right">37.73</td>
    <td align="right">13.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">68.63</td>
    <td align="right">61.58</td>
    <td align="right">46.93</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.07</td>
    <td align="right">20.90</td>
    <td align="right">25.71</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">25.58</td>
    <td align="right">22.11</td>
    <td align="right">26.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">112.90</td>
    <td align="right">118.21</td>
    <td align="right">51.69</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">26.05</td>
    <td align="right">24.05</td>
    <td align="right">30.56</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">34.45</td>
    <td align="right">26.51</td>
    <td align="right">29.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">242.21</td>
    <td align="right">130.59</td>
    <td align="right">49.62</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">33.34</td>
    <td align="right">34.58</td>
    <td align="right">36.35</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">44.63</td>
    <td align="right">34.91</td>
    <td align="right">40.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">405.81</td>
    <td align="right">327.84</td>
    <td align="right">82.90</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">62.11</td>
    <td align="right">48.23</td>
    <td align="right">49.30</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">36.91</td>
    <td align="right">32.75</td>
    <td align="right">47.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.66</td>
    <td align="right">42.73</td>
    <td align="right">42.57</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.80</td>
    <td align="right">45.27</td>
    <td align="right">44.07</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">23.86</td>
    <td align="right">40.29</td>
    <td align="right">40.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">60.18</td>
    <td align="right">73.33</td>
    <td align="right">71.53</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">71.97</td>
    <td align="right">89.96</td>
    <td align="right">83.39</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">26.00</td>
    <td align="right">56.04</td>
    <td align="right">39.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">54.70</td>
    <td align="right">94.17</td>
    <td align="right">96.18</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">66.41</td>
    <td align="right">108.45</td>
    <td align="right">97.28</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">90.56</td>
    <td align="right">118.52</td>
    <td align="right">88.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">74.32</td>
    <td align="right">103.99</td>
    <td align="right">109.05</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">76.67</td>
    <td align="right">123.23</td>
    <td align="right">128.69</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">86.59</td>
    <td align="right">136.76</td>
    <td align="right">121.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">31.63</td>
    <td align="right">46.01</td>
    <td align="right">40.20</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">23.93</td>
    <td align="right">64.19</td>
    <td align="right">44.53</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">26.05</td>
    <td align="right">41.57</td>
    <td align="right">46.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">45.24</td>
    <td align="right">55.83</td>
    <td align="right">43.50</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">20.22</td>
    <td align="right">59.23</td>
    <td align="right">39.87</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">22.91</td>
    <td align="right">56.42</td>
    <td align="right">44.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">30.25</td>
    <td align="right">59.80</td>
    <td align="right">43.65</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">34.41</td>
    <td align="right">56.13</td>
    <td align="right">38.39</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">33.02</td>
    <td align="right">64.96</td>
    <td align="right">53.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">43.34</td>
    <td align="right">66.97</td>
    <td align="right">47.76</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">41.10</td>
    <td align="right">87.46</td>
    <td align="right">54.23</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">37.00</td>
    <td align="right">71.32</td>
    <td align="right">57.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.95</td>
    <td align="right">43.40</td>
    <td align="right">38.38</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.44</td>
    <td align="right">53.98</td>
    <td align="right">43.79</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">40.87</td>
    <td align="right">60.78</td>
    <td align="right">60.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">38.69</td>
    <td align="right">61.02</td>
    <td align="right">37.76</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">46.40</td>
    <td align="right">67.41</td>
    <td align="right">40.19</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">48.28</td>
    <td align="right">78.80</td>
    <td align="right">78.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">46.87</td>
    <td align="right">76.67</td>
    <td align="right">44.85</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">52.88</td>
    <td align="right">81.51</td>
    <td align="right">41.83</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">51.41</td>
    <td align="right">88.11</td>
    <td align="right">85.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">68.08</td>
    <td align="right">114.41</td>
    <td align="right">58.70</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">101.71</td>
    <td align="right">109.61</td>
    <td align="right">59.65</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">83.23</td>
    <td align="right">134.82</td>
    <td align="right">139.91</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->

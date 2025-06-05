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
    <td align="right">26.21</td>
    <td align="right">4.55</td>
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
    <td align="right">10.97</td>
    <td align="right">10.74</td>
    <td align="right">16.71</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.78</td>
    <td align="right">4.07</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.89</td>
    <td align="right">5.23</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.11</td>
    <td align="right">15.89</td>
    <td align="right">17.76</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.86</td>
    <td align="right">4.99</td>
    <td align="right">5.03</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.53</td>
    <td align="right">5.56</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.50</td>
    <td align="right">18.64</td>
    <td align="right">16.67</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.49</td>
    <td align="right">5.36</td>
    <td align="right">5.37</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.32</td>
    <td align="right">6.37</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.88</td>
    <td align="right">24.03</td>
    <td align="right">16.91</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.25</td>
    <td align="right">5.98</td>
    <td align="right">6.00</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.78</td>
    <td align="right">6.66</td>
    <td align="right">6.65</td>
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
    <td align="right">5.12</td>
    <td align="right">5.75</td>
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.30</td>
    <td align="right">6.60</td>
    <td align="right">6.53</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.00</td>
    <td align="right">3.32</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.57</td>
    <td align="right">8.92</td>
    <td align="right">8.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.28</td>
    <td align="right">9.94</td>
    <td align="right">9.94</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.52</td>
    <td align="right">3.15</td>
    <td align="right">3.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.38</td>
    <td align="right">13.28</td>
    <td align="right">13.26</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.73</td>
    <td align="right">15.08</td>
    <td align="right">15.09</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.79</td>
    <td align="right">5.81</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.31</td>
    <td align="right">15.04</td>
    <td align="right">15.04</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.42</td>
    <td align="right">16.25</td>
    <td align="right">16.30</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.86</td>
    <td align="right">5.92</td>
    <td align="right">3.96</td>
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
    <td align="right">2.97</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.39</td>
    <td align="right">5.13</td>
    <td align="right">5.08</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.59</td>
    <td align="right">5.02</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.12</td>
    <td align="right">3.38</td>
    <td align="right">3.37</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.25</td>
    <td align="right">4.51</td>
    <td align="right">4.51</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.51</td>
    <td align="right">5.19</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.51</td>
    <td align="right">5.56</td>
    <td align="right">3.89</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.16</td>
    <td align="right">7.88</td>
    <td align="right">6.00</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.03</td>
    <td align="right">7.78</td>
    <td align="right">5.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.64</td>
    <td align="right">5.67</td>
    <td align="right">3.88</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.13</td>
    <td align="right">9.20</td>
    <td align="right">6.12</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.46</td>
    <td align="right">9.15</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">6.85</td>
    <td align="right">6.29</td>
    <td align="right">12.85</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">7.06</td>
    <td align="right">7.07</td>
    <td align="right">13.63</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.48</td>
    <td align="right">9.01</td>
    <td align="right">17.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.35</td>
    <td align="right">8.32</td>
    <td align="right">12.78</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.44</td>
    <td align="right">8.24</td>
    <td align="right">12.47</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.30</td>
    <td align="right">9.62</td>
    <td align="right">14.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.90</td>
    <td align="right">10.47</td>
    <td align="right">12.49</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.07</td>
    <td align="right">10.45</td>
    <td align="right">12.10</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.51</td>
    <td align="right">12.78</td>
    <td align="right">15.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.51</td>
    <td align="right">12.78</td>
    <td align="right">13.23</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.59</td>
    <td align="right">12.77</td>
    <td align="right">13.35</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">18.24</td>
    <td align="right">14.40</td>
    <td align="right">14.95</td>
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
    <td align="right">33.21</td>
    <td align="right">18.83</td>
    <td align="right">8.74</td>
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
    <td align="right">14.68</td>
    <td align="right">13.52</td>
    <td align="right">18.27</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.91</td>
    <td align="right">5.22</td>
    <td align="right">5.24</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.92</td>
    <td align="right">6.13</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.50</td>
    <td align="right">19.84</td>
    <td align="right">18.87</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.76</td>
    <td align="right">5.96</td>
    <td align="right">5.89</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">8.06</td>
    <td align="right">6.61</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">35.67</td>
    <td align="right">49.08</td>
    <td align="right">22.96</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.00</td>
    <td align="right">12.84</td>
    <td align="right">9.49</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.38</td>
    <td align="right">13.94</td>
    <td align="right">13.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">66.88</td>
    <td align="right">69.80</td>
    <td align="right">23.67</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.03</td>
    <td align="right">13.85</td>
    <td align="right">14.47</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.00</td>
    <td align="right">14.14</td>
    <td align="right">13.16</td>
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
    <td align="right">6.33</td>
    <td align="right">7.14</td>
    <td align="right">7.02</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.45</td>
    <td align="right">8.16</td>
    <td align="right">8.03</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.95</td>
    <td align="right">4.55</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.73</td>
    <td align="right">10.54</td>
    <td align="right">11.12</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.20</td>
    <td align="right">13.74</td>
    <td align="right">12.68</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.85</td>
    <td align="right">3.24</td>
    <td align="right">3.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">13.50</td>
    <td align="right">17.86</td>
    <td align="right">17.37</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.08</td>
    <td align="right">24.03</td>
    <td align="right">21.06</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.52</td>
    <td align="right">13.54</td>
    <td align="right">6.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">18.71</td>
    <td align="right">24.35</td>
    <td align="right">23.43</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.19</td>
    <td align="right">28.92</td>
    <td align="right">27.37</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">13.15</td>
    <td align="right">14.46</td>
    <td align="right">12.93</td>
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
    <td align="right">4.14</td>
    <td align="right">4.13</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.31</td>
    <td align="right">6.37</td>
    <td align="right">6.65</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.39</td>
    <td align="right">6.07</td>
    <td align="right">6.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.98</td>
    <td align="right">4.40</td>
    <td align="right">4.34</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.95</td>
    <td align="right">5.30</td>
    <td align="right">5.62</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.29</td>
    <td align="right">6.69</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">12.13</td>
    <td align="right">9.40</td>
    <td align="right">6.23</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.79</td>
    <td align="right">13.64</td>
    <td align="right">8.97</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.83</td>
    <td align="right">12.01</td>
    <td align="right">9.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.59</td>
    <td align="right">11.99</td>
    <td align="right">7.73</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">13.89</td>
    <td align="right">17.80</td>
    <td align="right">12.98</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.89</td>
    <td align="right">21.05</td>
    <td align="right">11.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">8.39</td>
    <td align="right">7.61</td>
    <td align="right">13.53</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.40</td>
    <td align="right">8.64</td>
    <td align="right">14.33</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.07</td>
    <td align="right">11.09</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.11</td>
    <td align="right">10.42</td>
    <td align="right">14.83</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">12.27</td>
    <td align="right">9.57</td>
    <td align="right">13.91</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">15.06</td>
    <td align="right">11.81</td>
    <td align="right">15.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.00</td>
    <td align="right">17.91</td>
    <td align="right">15.63</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">17.10</td>
    <td align="right">17.12</td>
    <td align="right">15.63</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">36.58</td>
    <td align="right">25.25</td>
    <td align="right">18.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">28.44</td>
    <td align="right">28.74</td>
    <td align="right">20.20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">27.35</td>
    <td align="right">32.99</td>
    <td align="right">21.68</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">47.69</td>
    <td align="right">33.34</td>
    <td align="right">19.98</td>
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
    <td align="right">26.96</td>
    <td align="right">4.39</td>
    <td align="right">3.44</td>
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
    <td align="right">9.19</td>
    <td align="right">9.14</td>
    <td align="right">15.34</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.65</td>
    <td align="right">3.95</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.85</td>
    <td align="right">4.63</td>
    <td align="right">4.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.19</td>
    <td align="right">13.41</td>
    <td align="right">16.57</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.10</td>
    <td align="right">4.58</td>
    <td align="right">4.56</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.49</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.46</td>
    <td align="right">16.72</td>
    <td align="right">15.57</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.50</td>
    <td align="right">5.06</td>
    <td align="right">5.25</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.65</td>
    <td align="right">6.01</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.30</td>
    <td align="right">22.80</td>
    <td align="right">17.12</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.57</td>
    <td align="right">5.69</td>
    <td align="right">5.87</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.85</td>
    <td align="right">3.32</td>
    <td align="right">3.34</td>
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
    <td align="right">3.06</td>
    <td align="right">3.59</td>
    <td align="right">3.60</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.19</td>
    <td align="right">3.52</td>
    <td align="right">3.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.64</td>
    <td align="right">2.51</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.75</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.77</td>
    <td align="right">4.39</td>
    <td align="right">4.43</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.14</td>
    <td align="right">2.27</td>
    <td align="right">2.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.58</td>
    <td align="right">7.10</td>
    <td align="right">7.34</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.80</td>
    <td align="right">7.16</td>
    <td align="right">7.19</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.22</td>
    <td align="right">4.46</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.05</td>
    <td align="right">7.62</td>
    <td align="right">7.70</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.40</td>
    <td align="right">8.14</td>
    <td align="right">8.22</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.25</td>
    <td align="right">4.40</td>
    <td align="right">3.19</td>
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
    <td align="right">2.60</td>
    <td align="right">2.37</td>
    <td align="right">2.35</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.66</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.69</td>
    <td align="right">3.94</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.69</td>
    <td align="right">2.45</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.94</td>
    <td align="right">3.73</td>
    <td align="right">3.74</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.86</td>
    <td align="right">4.06</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.22</td>
    <td align="right">4.30</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.71</td>
    <td align="right">6.09</td>
    <td align="right">4.69</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.80</td>
    <td align="right">6.04</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.30</td>
    <td align="right">4.35</td>
    <td align="right">2.96</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.67</td>
    <td align="right">7.14</td>
    <td align="right">4.72</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.79</td>
    <td align="right">7.06</td>
    <td align="right">4.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">6.65</td>
    <td align="right">6.10</td>
    <td align="right">12.43</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.82</td>
    <td align="right">6.08</td>
    <td align="right">12.19</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.46</td>
    <td align="right">7.97</td>
    <td align="right">16.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.31</td>
    <td align="right">8.46</td>
    <td align="right">12.33</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.76</td>
    <td align="right">7.58</td>
    <td align="right">11.81</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.75</td>
    <td align="right">9.55</td>
    <td align="right">13.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.89</td>
    <td align="right">9.93</td>
    <td align="right">12.08</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.51</td>
    <td align="right">9.94</td>
    <td align="right">11.82</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.98</td>
    <td align="right">12.39</td>
    <td align="right">14.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.39</td>
    <td align="right">12.22</td>
    <td align="right">12.80</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.89</td>
    <td align="right">12.26</td>
    <td align="right">12.83</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.77</td>
    <td align="right">13.79</td>
    <td align="right">14.53</td>
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
    <td align="right">32.45</td>
    <td align="right">15.96</td>
    <td align="right">6.52</td>
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
    <td align="right">11.25</td>
    <td align="right">10.92</td>
    <td align="right">16.59</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.70</td>
    <td align="right">4.99</td>
    <td align="right">4.75</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.02</td>
    <td align="right">5.44</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.40</td>
    <td align="right">15.99</td>
    <td align="right">17.41</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.01</td>
    <td align="right">5.47</td>
    <td align="right">5.30</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.38</td>
    <td align="right">6.27</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">24.44</td>
    <td align="right">24.32</td>
    <td align="right">18.83</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.48</td>
    <td align="right">7.45</td>
    <td align="right">7.36</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.66</td>
    <td align="right">7.90</td>
    <td align="right">9.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">38.65</td>
    <td align="right">39.53</td>
    <td align="right">18.49</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.00</td>
    <td align="right">11.23</td>
    <td align="right">9.40</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">5.15</td>
    <td align="right">6.11</td>
    <td align="right">5.80</td>
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
    <td align="right">3.66</td>
    <td align="right">4.28</td>
    <td align="right">4.41</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.81</td>
    <td align="right">4.33</td>
    <td align="right">4.32</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.11</td>
    <td align="right">3.13</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.20</td>
    <td align="right">4.66</td>
    <td align="right">4.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.32</td>
    <td align="right">5.74</td>
    <td align="right">5.56</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.78</td>
    <td align="right">3.49</td>
    <td align="right">3.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.49</td>
    <td align="right">10.85</td>
    <td align="right">10.27</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">8.36</td>
    <td align="right">10.64</td>
    <td align="right">11.00</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.09</td>
    <td align="right">6.63</td>
    <td align="right">4.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">9.65</td>
    <td align="right">13.44</td>
    <td align="right">12.97</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">11.78</td>
    <td align="right">16.99</td>
    <td align="right">17.26</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.46</td>
    <td align="right">11.29</td>
    <td align="right">5.32</td>
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
    <td align="right">3.15</td>
    <td align="right">2.99</td>
    <td align="right">3.00</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.36</td>
    <td align="right">4.96</td>
    <td align="right">4.93</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.38</td>
    <td align="right">4.78</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.16</td>
    <td align="right">3.07</td>
    <td align="right">2.97</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.67</td>
    <td align="right">4.47</td>
    <td align="right">4.51</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.68</td>
    <td align="right">5.00</td>
    <td align="right">5.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.68</td>
    <td align="right">6.74</td>
    <td align="right">4.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">7.99</td>
    <td align="right">8.43</td>
    <td align="right">7.30</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">8.17</td>
    <td align="right">8.33</td>
    <td align="right">6.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">8.08</td>
    <td align="right">9.51</td>
    <td align="right">7.62</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.69</td>
    <td align="right">14.26</td>
    <td align="right">8.70</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.95</td>
    <td align="right">12.23</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">8.12</td>
    <td align="right">7.16</td>
    <td align="right">13.22</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.18</td>
    <td align="right">7.18</td>
    <td align="right">12.83</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.87</td>
    <td align="right">9.28</td>
    <td align="right">17.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.43</td>
    <td align="right">9.41</td>
    <td align="right">12.77</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.97</td>
    <td align="right">9.13</td>
    <td align="right">12.67</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.90</td>
    <td align="right">10.72</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.14</td>
    <td align="right">12.33</td>
    <td align="right">13.17</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.72</td>
    <td align="right">12.75</td>
    <td align="right">14.67</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">18.14</td>
    <td align="right">15.74</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">20.00</td>
    <td align="right">17.84</td>
    <td align="right">14.87</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">22.28</td>
    <td align="right">16.60</td>
    <td align="right">15.03</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">31.54</td>
    <td align="right">23.51</td>
    <td align="right">16.57</td>
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
    <td align="right">21.06</td>
    <td align="right">3.72</td>
    <td align="right">2.40</td>
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
    <td align="right">7.39</td>
    <td align="right">4.98</td>
    <td align="right">12.49</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.44</td>
    <td align="right">1.33</td>
    <td align="right">1.36</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.71</td>
    <td align="right">1.40</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.63</td>
    <td align="right">7.59</td>
    <td align="right">12.88</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.44</td>
    <td align="right">1.48</td>
    <td align="right">1.48</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.80</td>
    <td align="right">1.56</td>
    <td align="right">1.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.82</td>
    <td align="right">9.37</td>
    <td align="right">12.16</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.91</td>
    <td align="right">1.82</td>
    <td align="right">2.00</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">3.48</td>
    <td align="right">1.95</td>
    <td align="right">1.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.33</td>
    <td align="right">12.01</td>
    <td align="right">12.45</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.05</td>
    <td align="right">2.07</td>
    <td align="right">1.92</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.96</td>
    <td align="right">1.75</td>
    <td align="right">1.76</td>
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
    <td align="right">2.39</td>
    <td align="right">1.79</td>
    <td align="right">1.82</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.81</td>
    <td align="right">2.00</td>
    <td align="right">1.93</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.23</td>
    <td align="right">1.90</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.55</td>
    <td align="right">2.18</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.06</td>
    <td align="right">2.40</td>
    <td align="right">2.91</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.66</td>
    <td align="right">1.51</td>
    <td align="right">3.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.51</td>
    <td align="right">3.49</td>
    <td align="right">3.21</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.37</td>
    <td align="right">3.24</td>
    <td align="right">3.39</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.60</td>
    <td align="right">2.76</td>
    <td align="right">1.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.27</td>
    <td align="right">4.09</td>
    <td align="right">8.39</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.38</td>
    <td align="right">4.88</td>
    <td align="right">3.92</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
    <td align="right">1.94</td>
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
    <td align="right">2.12</td>
    <td align="right">1.88</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.54</td>
    <td align="right">1.86</td>
    <td align="right">1.81</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.50</td>
    <td align="right">1.89</td>
    <td align="right">1.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.11</td>
    <td align="right">1.78</td>
    <td align="right">1.88</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.41</td>
    <td align="right">2.25</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.10</td>
    <td align="right">2.49</td>
    <td align="right">2.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.31</td>
    <td align="right">2.45</td>
    <td align="right">1.99</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.13</td>
    <td align="right">3.29</td>
    <td align="right">3.07</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.58</td>
    <td align="right">3.10</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.99</td>
    <td align="right">3.33</td>
    <td align="right">1.97</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.90</td>
    <td align="right">4.08</td>
    <td align="right">3.65</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.46</td>
    <td align="right">4.06</td>
    <td align="right">4.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">3.33</td>
    <td align="right">3.55</td>
    <td align="right">10.17</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.49</td>
    <td align="right">3.42</td>
    <td align="right">11.23</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.83</td>
    <td align="right">4.69</td>
    <td align="right">13.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.58</td>
    <td align="right">5.23</td>
    <td align="right">12.91</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">4.92</td>
    <td align="right">4.55</td>
    <td align="right">11.18</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">7.88</td>
    <td align="right">4.82</td>
    <td align="right">10.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">7.04</td>
    <td align="right">6.49</td>
    <td align="right">10.97</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.18</td>
    <td align="right">5.38</td>
    <td align="right">10.09</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">8.96</td>
    <td align="right">6.46</td>
    <td align="right">12.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">9.54</td>
    <td align="right">7.44</td>
    <td align="right">10.29</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">7.29</td>
    <td align="right">7.54</td>
    <td align="right">11.71</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">11.23</td>
    <td align="right">7.34</td>
    <td align="right">11.11</td>
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
    <td align="right">28.34</td>
    <td align="right">13.54</td>
    <td align="right">8.33</td>
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
    <td align="right">9.52</td>
    <td align="right">8.87</td>
    <td align="right">18.19</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.36</td>
    <td align="right">2.26</td>
    <td align="right">3.67</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.07</td>
    <td align="right">2.95</td>
    <td align="right">3.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">25.71</td>
    <td align="right">19.34</td>
    <td align="right">22.29</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.11</td>
    <td align="right">6.05</td>
    <td align="right">6.39</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.18</td>
    <td align="right">6.16</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">47.81</td>
    <td align="right">38.79</td>
    <td align="right">23.38</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.90</td>
    <td align="right">8.80</td>
    <td align="right">7.57</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.95</td>
    <td align="right">9.34</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">69.75</td>
    <td align="right">51.54</td>
    <td align="right">25.97</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.57</td>
    <td align="right">10.34</td>
    <td align="right">10.68</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.83</td>
    <td align="right">7.78</td>
    <td align="right">7.78</td>
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
    <td align="right">3.76</td>
    <td align="right">4.52</td>
    <td align="right">3.79</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.74</td>
    <td align="right">4.54</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.19</td>
    <td align="right">4.35</td>
    <td align="right">4.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.35</td>
    <td align="right">8.45</td>
    <td align="right">8.44</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.41</td>
    <td align="right">7.06</td>
    <td align="right">7.44</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.71</td>
    <td align="right">7.51</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">14.76</td>
    <td align="right">11.03</td>
    <td align="right">12.32</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">14.89</td>
    <td align="right">14.82</td>
    <td align="right">13.74</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.67</td>
    <td align="right">10.50</td>
    <td align="right">6.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">19.19</td>
    <td align="right">16.22</td>
    <td align="right">17.20</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.23</td>
    <td align="right">18.31</td>
    <td align="right">17.30</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">13.37</td>
    <td align="right">15.28</td>
    <td align="right">8.43</td>
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
    <td align="right">3.80</td>
    <td align="right">5.86</td>
    <td align="right">5.11</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.72</td>
    <td align="right">4.15</td>
    <td align="right">2.57</td>
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
    <td align="right">2.87</td>
    <td align="right">3.07</td>
    <td align="right">3.13</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.95</td>
    <td align="right">4.69</td>
    <td align="right">4.45</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.23</td>
    <td align="right">4.66</td>
    <td align="right">4.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.52</td>
    <td align="right">7.25</td>
    <td align="right">5.02</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.33</td>
    <td align="right">8.96</td>
    <td align="right">8.97</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.78</td>
    <td align="right">8.90</td>
    <td align="right">8.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.48</td>
    <td align="right">10.32</td>
    <td align="right">6.01</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.28</td>
    <td align="right">12.47</td>
    <td align="right">12.39</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.66</td>
    <td align="right">13.29</td>
    <td align="right">13.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">4.68</td>
    <td align="right">4.47</td>
    <td align="right">11.25</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">4.52</td>
    <td align="right">4.16</td>
    <td align="right">11.09</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.91</td>
    <td align="right">4.95</td>
    <td align="right">13.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.81</td>
    <td align="right">8.79</td>
    <td align="right">12.42</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.23</td>
    <td align="right">7.28</td>
    <td align="right">12.05</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.77</td>
    <td align="right">7.79</td>
    <td align="right">12.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">22.37</td>
    <td align="right">16.97</td>
    <td align="right">16.17</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">20.78</td>
    <td align="right">17.17</td>
    <td align="right">13.81</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.92</td>
    <td align="right">14.45</td>
    <td align="right">17.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">25.48</td>
    <td align="right">22.32</td>
    <td align="right">17.72</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">26.39</td>
    <td align="right">19.48</td>
    <td align="right">15.82</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">32.89</td>
    <td align="right">19.41</td>
    <td align="right">17.99</td>
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
    <td align="right">35.56</td>
    <td align="right">5.95</td>
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
    <td align="right">12.28</td>
    <td align="right">12.65</td>
    <td align="right">17.90</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.84</td>
    <td align="right">4.44</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.99</td>
    <td align="right">5.19</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.56</td>
    <td align="right">17.76</td>
    <td align="right">17.51</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.96</td>
    <td align="right">4.75</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.06</td>
    <td align="right">5.92</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.74</td>
    <td align="right">21.36</td>
    <td align="right">17.20</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.71</td>
    <td align="right">5.43</td>
    <td align="right">5.37</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.49</td>
    <td align="right">6.80</td>
    <td align="right">6.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.33</td>
    <td align="right">26.85</td>
    <td align="right">17.07</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.91</td>
    <td align="right">5.89</td>
    <td align="right">5.88</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.37</td>
    <td align="right">7.50</td>
    <td align="right">7.37</td>
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
    <td align="right">7.84</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.42</td>
    <td align="right">5.59</td>
    <td align="right">5.62</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.42</td>
    <td align="right">3.98</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.56</td>
    <td align="right">8.26</td>
    <td align="right">8.24</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.48</td>
    <td align="right">7.99</td>
    <td align="right">8.83</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.90</td>
    <td align="right">4.87</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.39</td>
    <td align="right">10.80</td>
    <td align="right">10.91</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">24.67</td>
    <td align="right">10.72</td>
    <td align="right">10.76</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.07</td>
    <td align="right">7.18</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.09</td>
    <td align="right">12.56</td>
    <td align="right">12.71</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">22.06</td>
    <td align="right">13.58</td>
    <td align="right">12.64</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.14</td>
    <td align="right">7.19</td>
    <td align="right">5.36</td>
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
    <td align="right">3.32</td>
    <td align="right">3.88</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.56</td>
    <td align="right">5.51</td>
    <td align="right">5.53</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.74</td>
    <td align="right">5.40</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.28</td>
    <td align="right">5.56</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.95</td>
    <td align="right">5.78</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.94</td>
    <td align="right">7.15</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.12</td>
    <td align="right">6.85</td>
    <td align="right">5.08</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.90</td>
    <td align="right">9.36</td>
    <td align="right">7.55</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">10.04</td>
    <td align="right">9.37</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.22</td>
    <td align="right">7.01</td>
    <td align="right">5.10</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.07</td>
    <td align="right">10.84</td>
    <td align="right">7.85</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.36</td>
    <td align="right">10.67</td>
    <td align="right">8.15</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">8.50</td>
    <td align="right">8.85</td>
    <td align="right">13.85</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.65</td>
    <td align="right">8.71</td>
    <td align="right">13.75</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.23</td>
    <td align="right">11.69</td>
    <td align="right">16.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.53</td>
    <td align="right">11.04</td>
    <td align="right">12.95</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.78</td>
    <td align="right">11.61</td>
    <td align="right">13.38</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.65</td>
    <td align="right">12.96</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">13.89</td>
    <td align="right">14.31</td>
    <td align="right">12.76</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.48</td>
    <td align="right">14.36</td>
    <td align="right">12.70</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">19.80</td>
    <td align="right">17.92</td>
    <td align="right">15.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">18.64</td>
    <td align="right">17.54</td>
    <td align="right">13.64</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.62</td>
    <td align="right">17.10</td>
    <td align="right">13.56</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.27</td>
    <td align="right">20.57</td>
    <td align="right">15.07</td>
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
    <td align="right">45.49</td>
    <td align="right">21.96</td>
    <td align="right">12.41</td>
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
    <td align="right">15.00</td>
    <td align="right">13.28</td>
    <td align="right">18.40</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.45</td>
    <td align="right">4.64</td>
    <td align="right">4.58</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.21</td>
    <td align="right">5.79</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.79</td>
    <td align="right">19.11</td>
    <td align="right">18.51</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.42</td>
    <td align="right">5.23</td>
    <td align="right">5.27</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.73</td>
    <td align="right">7.34</td>
    <td align="right">7.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">44.83</td>
    <td align="right">56.83</td>
    <td align="right">28.57</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">24.45</td>
    <td align="right">17.74</td>
    <td align="right">18.90</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">26.81</td>
    <td align="right">20.97</td>
    <td align="right">18.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">72.00</td>
    <td align="right">96.07</td>
    <td align="right">28.04</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.50</td>
    <td align="right">18.81</td>
    <td align="right">20.53</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">27.91</td>
    <td align="right">25.71</td>
    <td align="right">24.85</td>
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
    <td align="right">9.84</td>
    <td align="right">6.36</td>
    <td align="right">6.77</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">10.47</td>
    <td align="right">7.02</td>
    <td align="right">6.47</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.79</td>
    <td align="right">4.33</td>
    <td align="right">4.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">20.16</td>
    <td align="right">12.58</td>
    <td align="right">14.11</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">22.06</td>
    <td align="right">11.13</td>
    <td align="right">11.70</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.60</td>
    <td align="right">6.55</td>
    <td align="right">6.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">32.79</td>
    <td align="right">20.81</td>
    <td align="right">20.75</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">33.23</td>
    <td align="right">23.57</td>
    <td align="right">27.40</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.20</td>
    <td align="right">13.49</td>
    <td align="right">13.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">39.37</td>
    <td align="right">37.90</td>
    <td align="right">39.97</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">67.11</td>
    <td align="right">42.62</td>
    <td align="right">38.63</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.95</td>
    <td align="right">25.52</td>
    <td align="right">20.63</td>
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
    <td align="right">4.16</td>
    <td align="right">4.86</td>
    <td align="right">4.52</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.30</td>
    <td align="right">6.87</td>
    <td align="right">7.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.64</td>
    <td align="right">8.64</td>
    <td align="right">6.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">6.75</td>
    <td align="right">13.31</td>
    <td align="right">10.43</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">12.19</td>
    <td align="right">15.41</td>
    <td align="right">7.24</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">22.25</td>
    <td align="right">19.54</td>
    <td align="right">15.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">15.27</td>
    <td align="right">16.35</td>
    <td align="right">11.48</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">15.67</td>
    <td align="right">16.13</td>
    <td align="right">12.83</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">13.01</td>
    <td align="right">12.99</td>
    <td align="right">12.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">20.36</td>
    <td align="right">25.73</td>
    <td align="right">17.18</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">21.15</td>
    <td align="right">25.18</td>
    <td align="right">19.03</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">28.03</td>
    <td align="right">27.12</td>
    <td align="right">21.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">10.22</td>
    <td align="right">10.26</td>
    <td align="right">14.52</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.51</td>
    <td align="right">10.15</td>
    <td align="right">15.06</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.70</td>
    <td align="right">14.01</td>
    <td align="right">17.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">18.80</td>
    <td align="right">21.69</td>
    <td align="right">15.20</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">22.20</td>
    <td align="right">21.94</td>
    <td align="right">19.57</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">37.05</td>
    <td align="right">50.73</td>
    <td align="right">23.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">42.69</td>
    <td align="right">53.77</td>
    <td align="right">24.12</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">44.36</td>
    <td align="right">58.38</td>
    <td align="right">24.42</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">70.30</td>
    <td align="right">63.66</td>
    <td align="right">27.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">58.06</td>
    <td align="right">62.65</td>
    <td align="right">25.06</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">58.99</td>
    <td align="right">62.32</td>
    <td align="right">26.04</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">70.85</td>
    <td align="right">68.29</td>
    <td align="right">26.53</td>
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
    <td align="right">61.97</td>
    <td align="right">32.21</td>
    <td align="right">16.40</td>
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
    <td align="right">27.30</td>
    <td align="right">41.93</td>
    <td align="right">36.12</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.51</td>
    <td align="right">15.53</td>
    <td align="right">15.54</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.12</td>
    <td align="right">19.08</td>
    <td align="right">19.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.01</td>
    <td align="right">63.87</td>
    <td align="right">39.15</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.26</td>
    <td align="right">19.48</td>
    <td align="right">19.49</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.05</td>
    <td align="right">18.51</td>
    <td align="right">18.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.22</td>
    <td align="right">77.25</td>
    <td align="right">38.50</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.32</td>
    <td align="right">18.64</td>
    <td align="right">18.43</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.03</td>
    <td align="right">18.22</td>
    <td align="right">18.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">55.30</td>
    <td align="right">95.96</td>
    <td align="right">37.13</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.20</td>
    <td align="right">18.71</td>
    <td align="right">18.73</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.93</td>
    <td align="right">19.86</td>
    <td align="right">19.84</td>
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
    <td align="right">16.20</td>
    <td align="right">21.20</td>
    <td align="right">21.21</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.67</td>
    <td align="right">22.27</td>
    <td align="right">22.27</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.02</td>
    <td align="right">13.64</td>
    <td align="right">13.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.34</td>
    <td align="right">25.86</td>
    <td align="right">25.83</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.56</td>
    <td align="right">27.86</td>
    <td align="right">27.88</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.99</td>
    <td align="right">16.26</td>
    <td align="right">15.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.04</td>
    <td align="right">33.33</td>
    <td align="right">33.36</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.78</td>
    <td align="right">46.71</td>
    <td align="right">47.04</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.88</td>
    <td align="right">19.33</td>
    <td align="right">19.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.57</td>
    <td align="right">36.16</td>
    <td align="right">36.08</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.62</td>
    <td align="right">56.55</td>
    <td align="right">56.58</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">22.84</td>
    <td align="right">25.46</td>
    <td align="right">25.53</td>
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
    <td align="right">15.36</td>
    <td align="right">15.54</td>
    <td align="right">15.53</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.24</td>
    <td align="right">21.24</td>
    <td align="right">21.34</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.62</td>
    <td align="right">22.26</td>
    <td align="right">22.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.75</td>
    <td align="right">20.26</td>
    <td align="right">20.24</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.37</td>
    <td align="right">25.83</td>
    <td align="right">25.85</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.50</td>
    <td align="right">27.84</td>
    <td align="right">27.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.53</td>
    <td align="right">24.60</td>
    <td align="right">24.61</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.03</td>
    <td align="right">33.34</td>
    <td align="right">33.33</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.72</td>
    <td align="right">46.65</td>
    <td align="right">47.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.34</td>
    <td align="right">37.19</td>
    <td align="right">37.22</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.62</td>
    <td align="right">36.16</td>
    <td align="right">36.14</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.66</td>
    <td align="right">56.54</td>
    <td align="right">56.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">12.85</td>
    <td align="right">16.00</td>
    <td align="right">23.60</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.20</td>
    <td align="right">20.72</td>
    <td align="right">25.38</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.28</td>
    <td align="right">29.19</td>
    <td align="right">34.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.77</td>
    <td align="right">23.38</td>
    <td align="right">24.74</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.34</td>
    <td align="right">28.21</td>
    <td align="right">26.23</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.57</td>
    <td align="right">33.40</td>
    <td align="right">30.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.45</td>
    <td align="right">26.11</td>
    <td align="right">24.31</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.63</td>
    <td align="right">33.66</td>
    <td align="right">25.82</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">46.96</td>
    <td align="right">41.60</td>
    <td align="right">33.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">27.57</td>
    <td align="right">27.97</td>
    <td align="right">25.69</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.57</td>
    <td align="right">40.25</td>
    <td align="right">27.29</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">48.50</td>
    <td align="right">43.93</td>
    <td align="right">31.64</td>
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
    <td align="right">67.36</td>
    <td align="right">95.26</td>
    <td align="right">17.23</td>
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
    <td align="right">27.96</td>
    <td align="right">43.46</td>
    <td align="right">39.32</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.89</td>
    <td align="right">15.72</td>
    <td align="right">15.72</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.55</td>
    <td align="right">19.13</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.25</td>
    <td align="right">62.18</td>
    <td align="right">40.13</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.23</td>
    <td align="right">19.81</td>
    <td align="right">19.81</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.06</td>
    <td align="right">18.65</td>
    <td align="right">18.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">43.35</td>
    <td align="right">75.18</td>
    <td align="right">38.50</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.08</td>
    <td align="right">18.38</td>
    <td align="right">18.56</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">17.91</td>
    <td align="right">18.18</td>
    <td align="right">18.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">53.98</td>
    <td align="right">91.96</td>
    <td align="right">36.97</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">17.78</td>
    <td align="right">18.71</td>
    <td align="right">18.69</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">18.65</td>
    <td align="right">19.76</td>
    <td align="right">19.74</td>
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
    <td align="right">16.67</td>
    <td align="right">22.12</td>
    <td align="right">22.11</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.34</td>
    <td align="right">23.20</td>
    <td align="right">23.18</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.20</td>
    <td align="right">14.01</td>
    <td align="right">14.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.23</td>
    <td align="right">25.29</td>
    <td align="right">25.32</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.25</td>
    <td align="right">27.75</td>
    <td align="right">27.77</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.61</td>
    <td align="right">16.02</td>
    <td align="right">15.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.53</td>
    <td align="right">33.03</td>
    <td align="right">33.01</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">64.50</td>
    <td align="right">47.75</td>
    <td align="right">47.90</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.44</td>
    <td align="right">18.91</td>
    <td align="right">18.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">33.82</td>
    <td align="right">34.97</td>
    <td align="right">34.94</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">78.12</td>
    <td align="right">56.94</td>
    <td align="right">56.97</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">22.82</td>
    <td align="right">24.41</td>
    <td align="right">24.44</td>
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
    <td align="right">15.92</td>
    <td align="right">16.13</td>
    <td align="right">16.17</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.62</td>
    <td align="right">22.12</td>
    <td align="right">22.11</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.30</td>
    <td align="right">23.19</td>
    <td align="right">23.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.33</td>
    <td align="right">20.00</td>
    <td align="right">19.99</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.22</td>
    <td align="right">25.27</td>
    <td align="right">25.31</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.27</td>
    <td align="right">27.72</td>
    <td align="right">27.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">27.27</td>
    <td align="right">24.17</td>
    <td align="right">24.15</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.54</td>
    <td align="right">33.02</td>
    <td align="right">33.00</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">64.50</td>
    <td align="right">47.71</td>
    <td align="right">47.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">34.71</td>
    <td align="right">36.55</td>
    <td align="right">36.63</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">33.78</td>
    <td align="right">34.96</td>
    <td align="right">34.97</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">78.11</td>
    <td align="right">56.94</td>
    <td align="right">56.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">13.04</td>
    <td align="right">16.49</td>
    <td align="right">24.36</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.57</td>
    <td align="right">21.40</td>
    <td align="right">26.02</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">32.58</td>
    <td align="right">29.66</td>
    <td align="right">35.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.75</td>
    <td align="right">22.95</td>
    <td align="right">24.82</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">27.03</td>
    <td align="right">28.10</td>
    <td align="right">26.12</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">38.52</td>
    <td align="right">33.68</td>
    <td align="right">30.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">23.97</td>
    <td align="right">25.64</td>
    <td align="right">24.30</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">32.44</td>
    <td align="right">32.95</td>
    <td align="right">25.58</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">46.75</td>
    <td align="right">41.60</td>
    <td align="right">33.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">27.07</td>
    <td align="right">27.05</td>
    <td align="right">25.16</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.78</td>
    <td align="right">39.24</td>
    <td align="right">26.74</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">47.80</td>
    <td align="right">43.44</td>
    <td align="right">31.30</td>
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
    <td align="right">62.07</td>
    <td align="right">10.16</td>
    <td align="right">6.88</td>
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
    <td align="right">13.78</td>
    <td align="right">22.59</td>
    <td align="right">26.45</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.32</td>
    <td align="right">12.35</td>
    <td align="right">12.36</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.63</td>
    <td align="right">13.77</td>
    <td align="right">13.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.41</td>
    <td align="right">35.06</td>
    <td align="right">29.11</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.14</td>
    <td align="right">14.05</td>
    <td align="right">14.47</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.70</td>
    <td align="right">15.31</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.85</td>
    <td align="right">47.27</td>
    <td align="right">29.28</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.74</td>
    <td align="right">15.38</td>
    <td align="right">15.46</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.27</td>
    <td align="right">16.71</td>
    <td align="right">16.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.02</td>
    <td align="right">60.27</td>
    <td align="right">30.98</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">16.17</td>
    <td align="right">16.29</td>
    <td align="right">16.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">17.31</td>
    <td align="right">17.83</td>
    <td align="right">17.81</td>
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
    <td align="right">12.81</td>
    <td align="right">16.07</td>
    <td align="right">16.09</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.22</td>
    <td align="right">16.68</td>
    <td align="right">16.68</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">6.99</td>
    <td align="right">9.36</td>
    <td align="right">9.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.46</td>
    <td align="right">22.40</td>
    <td align="right">22.48</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.76</td>
    <td align="right">22.37</td>
    <td align="right">22.36</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.39</td>
    <td align="right">14.19</td>
    <td align="right">14.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.95</td>
    <td align="right">32.16</td>
    <td align="right">32.14</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.69</td>
    <td align="right">30.85</td>
    <td align="right">30.81</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">12.99</td>
    <td align="right">17.50</td>
    <td align="right">17.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.90</td>
    <td align="right">35.75</td>
    <td align="right">35.79</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.05</td>
    <td align="right">35.82</td>
    <td align="right">35.77</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.32</td>
    <td align="right">20.46</td>
    <td align="right">20.47</td>
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
    <td align="right">6.56</td>
    <td align="right">9.40</td>
    <td align="right">9.39</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.77</td>
    <td align="right">16.09</td>
    <td align="right">16.06</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.74</td>
    <td align="right">16.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.39</td>
    <td align="right">13.71</td>
    <td align="right">13.72</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.39</td>
    <td align="right">22.54</td>
    <td align="right">22.55</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.78</td>
    <td align="right">22.36</td>
    <td align="right">22.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.47</td>
    <td align="right">17.63</td>
    <td align="right">17.65</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.00</td>
    <td align="right">32.13</td>
    <td align="right">32.11</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.70</td>
    <td align="right">30.83</td>
    <td align="right">30.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.07</td>
    <td align="right">20.97</td>
    <td align="right">20.84</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.97</td>
    <td align="right">35.78</td>
    <td align="right">35.80</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.04</td>
    <td align="right">35.81</td>
    <td align="right">35.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">12.09</td>
    <td align="right">10.80</td>
    <td align="right">18.81</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.55</td>
    <td align="right">16.29</td>
    <td align="right">20.01</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.85</td>
    <td align="right">33.79</td>
    <td align="right">36.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">15.24</td>
    <td align="right">16.24</td>
    <td align="right">19.21</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.76</td>
    <td align="right">23.44</td>
    <td align="right">20.67</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">53.81</td>
    <td align="right">37.10</td>
    <td align="right">35.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">17.93</td>
    <td align="right">18.88</td>
    <td align="right">18.59</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.02</td>
    <td align="right">29.99</td>
    <td align="right">20.56</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.69</td>
    <td align="right">45.55</td>
    <td align="right">38.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">20.15</td>
    <td align="right">21.26</td>
    <td align="right">19.84</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">30.15</td>
    <td align="right">35.70</td>
    <td align="right">21.49</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">65.21</td>
    <td align="right">47.34</td>
    <td align="right">37.25</td>
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
    <td align="right">48.00</td>
    <td align="right">10.86</td>
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
    <td align="right">14.13</td>
    <td align="right">22.87</td>
    <td align="right">28.27</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">10.51</td>
    <td align="right">12.50</td>
    <td align="right">12.52</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.51</td>
    <td align="right">14.00</td>
    <td align="right">14.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.39</td>
    <td align="right">34.48</td>
    <td align="right">29.92</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.36</td>
    <td align="right">13.90</td>
    <td align="right">13.88</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">14.66</td>
    <td align="right">15.34</td>
    <td align="right">15.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.73</td>
    <td align="right">47.54</td>
    <td align="right">29.78</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.53</td>
    <td align="right">19.26</td>
    <td align="right">15.01</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">16.41</td>
    <td align="right">16.32</td>
    <td align="right">16.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">32.13</td>
    <td align="right">66.19</td>
    <td align="right">32.78</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">17.80</td>
    <td align="right">17.60</td>
    <td align="right">16.88</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">19.42</td>
    <td align="right">19.08</td>
    <td align="right">19.43</td>
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
    <td align="right">13.04</td>
    <td align="right">16.64</td>
    <td align="right">16.63</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.33</td>
    <td align="right">17.41</td>
    <td align="right">17.45</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.18</td>
    <td align="right">9.39</td>
    <td align="right">9.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.01</td>
    <td align="right">22.21</td>
    <td align="right">22.15</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.96</td>
    <td align="right">22.08</td>
    <td align="right">22.21</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.37</td>
    <td align="right">14.19</td>
    <td align="right">13.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.41</td>
    <td align="right">33.14</td>
    <td align="right">33.00</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.63</td>
    <td align="right">31.16</td>
    <td align="right">31.25</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">12.99</td>
    <td align="right">16.92</td>
    <td align="right">16.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">28.73</td>
    <td align="right">38.20</td>
    <td align="right">38.26</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">35.22</td>
    <td align="right">37.43</td>
    <td align="right">37.13</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">18.05</td>
    <td align="right">24.46</td>
    <td align="right">23.31</td>
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
    <td align="right">6.68</td>
    <td align="right">9.50</td>
    <td align="right">9.53</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.03</td>
    <td align="right">16.65</td>
    <td align="right">16.62</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.30</td>
    <td align="right">17.44</td>
    <td align="right">17.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.38</td>
    <td align="right">13.47</td>
    <td align="right">13.47</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.93</td>
    <td align="right">22.04</td>
    <td align="right">22.16</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.04</td>
    <td align="right">22.14</td>
    <td align="right">22.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">12.95</td>
    <td align="right">17.13</td>
    <td align="right">17.09</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.88</td>
    <td align="right">32.92</td>
    <td align="right">33.39</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.16</td>
    <td align="right">31.44</td>
    <td align="right">31.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">18.23</td>
    <td align="right">23.05</td>
    <td align="right">24.09</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">28.69</td>
    <td align="right">38.37</td>
    <td align="right">37.82</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.93</td>
    <td align="right">37.05</td>
    <td align="right">37.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">12.14</td>
    <td align="right">10.93</td>
    <td align="right">18.95</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.40</td>
    <td align="right">16.57</td>
    <td align="right">20.31</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.17</td>
    <td align="right">33.03</td>
    <td align="right">36.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">15.12</td>
    <td align="right">16.08</td>
    <td align="right">19.27</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">19.89</td>
    <td align="right">23.30</td>
    <td align="right">20.75</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">54.75</td>
    <td align="right">48.07</td>
    <td align="right">38.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">18.29</td>
    <td align="right">18.84</td>
    <td align="right">18.61</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">24.17</td>
    <td align="right">30.34</td>
    <td align="right">21.02</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">64.76</td>
    <td align="right">48.39</td>
    <td align="right">36.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">21.16</td>
    <td align="right">23.75</td>
    <td align="right">21.21</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">33.32</td>
    <td align="right">41.48</td>
    <td align="right">22.95</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">77.01</td>
    <td align="right">54.89</td>
    <td align="right">41.55</td>
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
    <td align="right">43.18</td>
    <td align="right">8.63</td>
    <td align="right">6.58</td>
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
    <td align="right">59.62</td>
    <td align="right">54.65</td>
    <td align="right">41.48</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">20.99</td>
    <td align="right">19.72</td>
    <td align="right">23.23</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.97</td>
    <td align="right">21.51</td>
    <td align="right">24.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.96</td>
    <td align="right">80.32</td>
    <td align="right">44.03</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.31</td>
    <td align="right">21.23</td>
    <td align="right">23.77</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.15</td>
    <td align="right">22.32</td>
    <td align="right">24.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">111.47</td>
    <td align="right">100.77</td>
    <td align="right">45.80</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.57</td>
    <td align="right">22.67</td>
    <td align="right">24.27</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.81</td>
    <td align="right">24.19</td>
    <td align="right">25.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">141.46</td>
    <td align="right">125.87</td>
    <td align="right">45.44</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.08</td>
    <td align="right">24.31</td>
    <td align="right">25.34</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.92</td>
    <td align="right">25.57</td>
    <td align="right">26.36</td>
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
    <td align="right">23.15</td>
    <td align="right">41.25</td>
    <td align="right">41.40</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">28.72</td>
    <td align="right">41.36</td>
    <td align="right">41.48</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.56</td>
    <td align="right">25.51</td>
    <td align="right">25.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">27.82</td>
    <td align="right">56.79</td>
    <td align="right">56.97</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">34.28</td>
    <td align="right">57.86</td>
    <td align="right">57.95</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.65</td>
    <td align="right">36.33</td>
    <td align="right">25.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.45</td>
    <td align="right">76.46</td>
    <td align="right">76.53</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.83</td>
    <td align="right">77.75</td>
    <td align="right">77.85</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.07</td>
    <td align="right">55.13</td>
    <td align="right">39.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.96</td>
    <td align="right">86.27</td>
    <td align="right">86.26</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">50.26</td>
    <td align="right">92.34</td>
    <td align="right">92.32</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.23</td>
    <td align="right">55.72</td>
    <td align="right">40.27</td>
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
    <td align="right">18.55</td>
    <td align="right">26.09</td>
    <td align="right">26.34</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.63</td>
    <td align="right">29.26</td>
    <td align="right">29.24</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.87</td>
    <td align="right">30.96</td>
    <td align="right">30.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.02</td>
    <td align="right">46.67</td>
    <td align="right">35.17</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.40</td>
    <td align="right">39.92</td>
    <td align="right">27.86</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.97</td>
    <td align="right">51.94</td>
    <td align="right">40.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.72</td>
    <td align="right">54.60</td>
    <td align="right">38.73</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.14</td>
    <td align="right">53.09</td>
    <td align="right">35.33</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.37</td>
    <td align="right">61.34</td>
    <td align="right">43.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.80</td>
    <td align="right">55.51</td>
    <td align="right">39.46</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.77</td>
    <td align="right">64.64</td>
    <td align="right">44.77</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.24</td>
    <td align="right">64.29</td>
    <td align="right">44.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">23.03</td>
    <td align="right">22.39</td>
    <td align="right">29.45</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.08</td>
    <td align="right">42.80</td>
    <td align="right">34.95</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.95</td>
    <td align="right">53.19</td>
    <td align="right">40.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">32.52</td>
    <td align="right">32.90</td>
    <td align="right">30.55</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.70</td>
    <td align="right">61.25</td>
    <td align="right">35.84</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.11</td>
    <td align="right">60.99</td>
    <td align="right">38.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">37.99</td>
    <td align="right">37.90</td>
    <td align="right">30.21</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.89</td>
    <td align="right">73.66</td>
    <td align="right">35.66</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">49.27</td>
    <td align="right">78.41</td>
    <td align="right">41.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">44.77</td>
    <td align="right">47.70</td>
    <td align="right">31.42</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">52.66</td>
    <td align="right">93.58</td>
    <td align="right">37.42</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.70</td>
    <td align="right">94.62</td>
    <td align="right">39.34</td>
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
    <td align="right">60.02</td>
    <td align="right">34.82</td>
    <td align="right">10.52</td>
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
    <td align="right">67.14</td>
    <td align="right">59.88</td>
    <td align="right">46.26</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">22.83</td>
    <td align="right">20.85</td>
    <td align="right">25.65</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">25.47</td>
    <td align="right">22.07</td>
    <td align="right">26.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">97.23</td>
    <td align="right">85.20</td>
    <td align="right">47.64</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">24.83</td>
    <td align="right">21.94</td>
    <td align="right">24.82</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.90</td>
    <td align="right">22.93</td>
    <td align="right">25.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">124.90</td>
    <td align="right">112.58</td>
    <td align="right">49.67</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">27.89</td>
    <td align="right">23.63</td>
    <td align="right">25.30</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">32.48</td>
    <td align="right">25.81</td>
    <td align="right">27.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">173.77</td>
    <td align="right">151.92</td>
    <td align="right">51.10</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">32.53</td>
    <td align="right">27.30</td>
    <td align="right">29.36</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">37.55</td>
    <td align="right">28.98</td>
    <td align="right">30.25</td>
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
    <td align="right">25.24</td>
    <td align="right">41.97</td>
    <td align="right">41.91</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.55</td>
    <td align="right">41.97</td>
    <td align="right">42.07</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.02</td>
    <td align="right">30.43</td>
    <td align="right">30.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">29.98</td>
    <td align="right">57.27</td>
    <td align="right">57.47</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.30</td>
    <td align="right">58.62</td>
    <td align="right">59.00</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.06</td>
    <td align="right">40.59</td>
    <td align="right">29.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">44.38</td>
    <td align="right">78.61</td>
    <td align="right">78.47</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">48.71</td>
    <td align="right">79.83</td>
    <td align="right">79.88</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">32.16</td>
    <td align="right">60.83</td>
    <td align="right">44.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">50.43</td>
    <td align="right">90.46</td>
    <td align="right">90.62</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">57.71</td>
    <td align="right">97.65</td>
    <td align="right">97.82</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">37.30</td>
    <td align="right">65.37</td>
    <td align="right">49.41</td>
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
    <td align="right">19.82</td>
    <td align="right">31.40</td>
    <td align="right">31.36</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.73</td>
    <td align="right">33.55</td>
    <td align="right">33.58</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">21.76</td>
    <td align="right">35.75</td>
    <td align="right">35.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.02</td>
    <td align="right">50.50</td>
    <td align="right">39.45</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.16</td>
    <td align="right">42.61</td>
    <td align="right">30.52</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">21.85</td>
    <td align="right">56.36</td>
    <td align="right">44.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">30.36</td>
    <td align="right">59.40</td>
    <td align="right">43.08</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">34.89</td>
    <td align="right">57.18</td>
    <td align="right">38.94</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">33.82</td>
    <td align="right">66.11</td>
    <td align="right">47.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">35.28</td>
    <td align="right">64.09</td>
    <td align="right">47.59</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">37.96</td>
    <td align="right">71.60</td>
    <td align="right">50.48</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">37.09</td>
    <td align="right">71.64</td>
    <td align="right">55.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">25.29</td>
    <td align="right">24.59</td>
    <td align="right">32.50</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.37</td>
    <td align="right">43.36</td>
    <td align="right">38.29</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.43</td>
    <td align="right">53.92</td>
    <td align="right">43.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">35.05</td>
    <td align="right">35.62</td>
    <td align="right">32.68</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">38.51</td>
    <td align="right">62.27</td>
    <td align="right">38.20</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">45.09</td>
    <td align="right">62.00</td>
    <td align="right">40.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">43.40</td>
    <td align="right">42.04</td>
    <td align="right">33.68</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">44.34</td>
    <td align="right">75.19</td>
    <td align="right">37.85</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">54.39</td>
    <td align="right">81.64</td>
    <td align="right">44.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">54.77</td>
    <td align="right">55.60</td>
    <td align="right">36.54</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">59.09</td>
    <td align="right">101.55</td>
    <td align="right">42.45</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">72.54</td>
    <td align="right">103.64</td>
    <td align="right">46.90</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->

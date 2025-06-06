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
    <td align="right">26.84</td>
    <td align="right">4.64</td>
    <td align="right">3.60</td>
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
    <td align="right">11.24</td>
    <td align="right">10.70</td>
    <td align="right">16.68</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.02</td>
    <td align="right">4.36</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.89</td>
    <td align="right">5.11</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.67</td>
    <td align="right">15.79</td>
    <td align="right">17.70</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.89</td>
    <td align="right">4.99</td>
    <td align="right">5.05</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.45</td>
    <td align="right">5.54</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.50</td>
    <td align="right">18.62</td>
    <td align="right">16.58</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.46</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.26</td>
    <td align="right">6.37</td>
    <td align="right">6.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.98</td>
    <td align="right">23.24</td>
    <td align="right">16.89</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.22</td>
    <td align="right">5.97</td>
    <td align="right">6.00</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.76</td>
    <td align="right">6.72</td>
    <td align="right">6.69</td>
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
    <td align="right">5.14</td>
    <td align="right">5.81</td>
    <td align="right">5.81</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.34</td>
    <td align="right">6.59</td>
    <td align="right">6.50</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.99</td>
    <td align="right">3.14</td>
    <td align="right">3.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.53</td>
    <td align="right">8.92</td>
    <td align="right">8.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.26</td>
    <td align="right">9.92</td>
    <td align="right">9.90</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.51</td>
    <td align="right">3.15</td>
    <td align="right">3.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.29</td>
    <td align="right">13.85</td>
    <td align="right">13.87</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.71</td>
    <td align="right">14.14</td>
    <td align="right">14.10</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.81</td>
    <td align="right">5.79</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.10</td>
    <td align="right">15.62</td>
    <td align="right">15.66</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.33</td>
    <td align="right">17.49</td>
    <td align="right">17.44</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.84</td>
    <td align="right">5.89</td>
    <td align="right">3.91</td>
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
    <td align="right">3.25</td>
    <td align="right">3.22</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.39</td>
    <td align="right">5.15</td>
    <td align="right">5.07</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.61</td>
    <td align="right">5.00</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.06</td>
    <td align="right">3.32</td>
    <td align="right">3.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.21</td>
    <td align="right">4.51</td>
    <td align="right">4.52</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.48</td>
    <td align="right">5.14</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.49</td>
    <td align="right">5.56</td>
    <td align="right">3.82</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.09</td>
    <td align="right">7.86</td>
    <td align="right">5.98</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.88</td>
    <td align="right">7.64</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.47</td>
    <td align="right">5.56</td>
    <td align="right">3.81</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.05</td>
    <td align="right">9.16</td>
    <td align="right">5.96</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.31</td>
    <td align="right">9.07</td>
    <td align="right">5.95</td>
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
    <td align="right">6.88</td>
    <td align="right">6.99</td>
    <td align="right">13.55</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.44</td>
    <td align="right">8.91</td>
    <td align="right">17.38</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.52</td>
    <td align="right">11.49</td>
    <td align="right">11.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.30</td>
    <td align="right">8.32</td>
    <td align="right">12.35</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.15</td>
    <td align="right">9.46</td>
    <td align="right">14.26</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.30</td>
    <td align="right">14.79</td>
    <td align="right">14.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.95</td>
    <td align="right">10.41</td>
    <td align="right">12.07</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.35</td>
    <td align="right">12.69</td>
    <td align="right">15.25</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.17</td>
    <td align="right">16.79</td>
    <td align="right">17.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.43</td>
    <td align="right">12.81</td>
    <td align="right">13.19</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.70</td>
    <td align="right">14.21</td>
    <td align="right">14.91</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">21.87</td>
    <td align="right">22.58</td>
    <td align="right">22.65</td>
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
    <td align="right">32.49</td>
    <td align="right">18.86</td>
    <td align="right">7.30</td>
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
    <td align="right">12.83</td>
    <td align="right">12.01</td>
    <td align="right">17.22</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.55</td>
    <td align="right">4.79</td>
    <td align="right">4.79</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.48</td>
    <td align="right">5.68</td>
    <td align="right">5.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">17.84</td>
    <td align="right">16.98</td>
    <td align="right">17.93</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.26</td>
    <td align="right">5.34</td>
    <td align="right">5.41</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.01</td>
    <td align="right">6.08</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.86</td>
    <td align="right">28.16</td>
    <td align="right">18.47</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">8.15</td>
    <td align="right">8.00</td>
    <td align="right">7.85</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.10</td>
    <td align="right">9.40</td>
    <td align="right">9.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">68.94</td>
    <td align="right">70.09</td>
    <td align="right">22.59</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.57</td>
    <td align="right">14.83</td>
    <td align="right">15.61</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.73</td>
    <td align="right">15.62</td>
    <td align="right">16.43</td>
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
    <td align="right">5.69</td>
    <td align="right">6.48</td>
    <td align="right">6.47</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.93</td>
    <td align="right">7.48</td>
    <td align="right">7.55</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.41</td>
    <td align="right">3.81</td>
    <td align="right">3.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.95</td>
    <td align="right">9.44</td>
    <td align="right">9.51</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.75</td>
    <td align="right">11.56</td>
    <td align="right">11.12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.00</td>
    <td align="right">3.92</td>
    <td align="right">4.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.50</td>
    <td align="right">19.79</td>
    <td align="right">16.59</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.73</td>
    <td align="right">17.90</td>
    <td align="right">17.36</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.34</td>
    <td align="right">9.19</td>
    <td align="right">6.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">22.55</td>
    <td align="right">26.27</td>
    <td align="right">26.62</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">27.10</td>
    <td align="right">29.76</td>
    <td align="right">30.16</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">14.73</td>
    <td align="right">15.08</td>
    <td align="right">8.75</td>
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
    <td align="right">3.32</td>
    <td align="right">3.70</td>
    <td align="right">3.72</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.94</td>
    <td align="right">5.71</td>
    <td align="right">5.64</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.08</td>
    <td align="right">5.53</td>
    <td align="right">5.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.27</td>
    <td align="right">3.58</td>
    <td align="right">3.59</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.53</td>
    <td align="right">4.90</td>
    <td align="right">4.93</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.92</td>
    <td align="right">5.67</td>
    <td align="right">5.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.79</td>
    <td align="right">9.23</td>
    <td align="right">6.65</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.35</td>
    <td align="right">12.62</td>
    <td align="right">8.85</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.14</td>
    <td align="right">11.46</td>
    <td align="right">8.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">12.43</td>
    <td align="right">14.04</td>
    <td align="right">9.61</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">17.27</td>
    <td align="right">21.09</td>
    <td align="right">13.16</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">15.66</td>
    <td align="right">22.14</td>
    <td align="right">15.12</td>
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
    <td align="right">7.70</td>
    <td align="right">7.78</td>
    <td align="right">13.84</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.22</td>
    <td align="right">9.82</td>
    <td align="right">18.03</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">11.99</td>
    <td align="right">12.86</td>
    <td align="right">12.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.28</td>
    <td align="right">9.18</td>
    <td align="right">13.07</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.80</td>
    <td align="right">11.47</td>
    <td align="right">15.19</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.74</td>
    <td align="right">17.61</td>
    <td align="right">17.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">23.49</td>
    <td align="right">16.45</td>
    <td align="right">14.91</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">26.74</td>
    <td align="right">24.86</td>
    <td align="right">18.58</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">19.25</td>
    <td align="right">19.41</td>
    <td align="right">19.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">32.64</td>
    <td align="right">24.84</td>
    <td align="right">18.37</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">46.25</td>
    <td align="right">34.14</td>
    <td align="right">20.85</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">34.46</td>
    <td align="right">36.90</td>
    <td align="right">35.27</td>
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
    <td align="right">26.72</td>
    <td align="right">4.14</td>
    <td align="right">3.37</td>
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
    <td align="right">9.31</td>
    <td align="right">9.00</td>
    <td align="right">15.42</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.34</td>
    <td align="right">3.97</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.87</td>
    <td align="right">4.69</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.16</td>
    <td align="right">13.52</td>
    <td align="right">16.64</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.57</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.49</td>
    <td align="right">5.52</td>
    <td align="right">5.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.42</td>
    <td align="right">16.72</td>
    <td align="right">15.73</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.41</td>
    <td align="right">5.14</td>
    <td align="right">5.16</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.99</td>
    <td align="right">6.06</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.37</td>
    <td align="right">21.15</td>
    <td align="right">16.13</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.83</td>
    <td align="right">5.69</td>
    <td align="right">5.70</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.90</td>
    <td align="right">3.33</td>
    <td align="right">3.33</td>
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
    <td align="right">3.05</td>
    <td align="right">3.59</td>
    <td align="right">3.62</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.17</td>
    <td align="right">3.51</td>
    <td align="right">3.50</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.63</td>
    <td align="right">2.50</td>
    <td align="right">2.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.73</td>
    <td align="right">4.09</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.70</td>
    <td align="right">4.37</td>
    <td align="right">4.39</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.14</td>
    <td align="right">2.26</td>
    <td align="right">2.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.62</td>
    <td align="right">7.17</td>
    <td align="right">7.19</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.82</td>
    <td align="right">7.09</td>
    <td align="right">7.06</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.21</td>
    <td align="right">4.36</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.02</td>
    <td align="right">7.81</td>
    <td align="right">7.80</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.35</td>
    <td align="right">8.26</td>
    <td align="right">8.13</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.22</td>
    <td align="right">4.39</td>
    <td align="right">3.14</td>
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
    <td align="right">2.62</td>
    <td align="right">2.37</td>
    <td align="right">2.41</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.60</td>
    <td align="right">4.08</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.75</td>
    <td align="right">3.92</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.70</td>
    <td align="right">2.39</td>
    <td align="right">2.40</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.89</td>
    <td align="right">3.74</td>
    <td align="right">3.75</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.83</td>
    <td align="right">4.03</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.25</td>
    <td align="right">4.30</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.61</td>
    <td align="right">6.16</td>
    <td align="right">4.74</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.69</td>
    <td align="right">5.90</td>
    <td align="right">4.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.28</td>
    <td align="right">4.32</td>
    <td align="right">2.92</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.78</td>
    <td align="right">7.11</td>
    <td align="right">4.88</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.96</td>
    <td align="right">7.19</td>
    <td align="right">4.67</td>
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
    <td align="right">6.74</td>
    <td align="right">6.15</td>
    <td align="right">12.22</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.35</td>
    <td align="right">8.03</td>
    <td align="right">16.60</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.62</td>
    <td align="right">11.15</td>
    <td align="right">11.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.49</td>
    <td align="right">8.23</td>
    <td align="right">12.07</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.70</td>
    <td align="right">9.56</td>
    <td align="right">14.11</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">16.11</td>
    <td align="right">16.46</td>
    <td align="right">16.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.74</td>
    <td align="right">10.32</td>
    <td align="right">12.04</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.54</td>
    <td align="right">12.73</td>
    <td align="right">14.91</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">18.94</td>
    <td align="right">19.33</td>
    <td align="right">19.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.89</td>
    <td align="right">12.32</td>
    <td align="right">12.68</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">18.16</td>
    <td align="right">13.88</td>
    <td align="right">14.66</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">25.86</td>
    <td align="right">25.61</td>
    <td align="right">25.44</td>
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
    <td align="right">30.69</td>
    <td align="right">15.76</td>
    <td align="right">5.96</td>
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
    <td align="right">11.13</td>
    <td align="right">11.04</td>
    <td align="right">16.65</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.03</td>
    <td align="right">4.70</td>
    <td align="right">4.85</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.75</td>
    <td align="right">5.61</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.18</td>
    <td align="right">15.54</td>
    <td align="right">17.29</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.37</td>
    <td align="right">5.07</td>
    <td align="right">5.23</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.14</td>
    <td align="right">6.09</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">21.45</td>
    <td align="right">27.29</td>
    <td align="right">18.19</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.39</td>
    <td align="right">5.99</td>
    <td align="right">6.50</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.52</td>
    <td align="right">7.98</td>
    <td align="right">7.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">38.65</td>
    <td align="right">43.76</td>
    <td align="right">19.72</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.08</td>
    <td align="right">8.93</td>
    <td align="right">9.47</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.92</td>
    <td align="right">7.47</td>
    <td align="right">5.75</td>
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
    <td align="right">3.70</td>
    <td align="right">4.35</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.83</td>
    <td align="right">4.29</td>
    <td align="right">4.32</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.13</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.28</td>
    <td align="right">4.70</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.76</td>
    <td align="right">4.34</td>
    <td align="right">4.33</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.53</td>
    <td align="right">2.68</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">7.07</td>
    <td align="right">9.06</td>
    <td align="right">9.01</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.09</td>
    <td align="right">9.15</td>
    <td align="right">9.16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.08</td>
    <td align="right">5.08</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">9.60</td>
    <td align="right">12.18</td>
    <td align="right">13.62</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">8.11</td>
    <td align="right">10.87</td>
    <td align="right">10.66</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">5.94</td>
    <td align="right">6.61</td>
    <td align="right">4.71</td>
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
    <td align="right">3.01</td>
    <td align="right">3.00</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.30</td>
    <td align="right">4.92</td>
    <td align="right">4.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.48</td>
    <td align="right">4.79</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.09</td>
    <td align="right">2.97</td>
    <td align="right">2.98</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.39</td>
    <td align="right">4.31</td>
    <td align="right">4.32</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.31</td>
    <td align="right">4.71</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.20</td>
    <td align="right">5.58</td>
    <td align="right">3.91</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.90</td>
    <td align="right">7.79</td>
    <td align="right">6.46</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.05</td>
    <td align="right">7.66</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">5.90</td>
    <td align="right">6.23</td>
    <td align="right">4.64</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">9.09</td>
    <td align="right">10.25</td>
    <td align="right">7.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">9.26</td>
    <td align="right">9.81</td>
    <td align="right">6.71</td>
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
    <td align="right">8.06</td>
    <td align="right">7.24</td>
    <td align="right">12.73</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">11.95</td>
    <td align="right">9.34</td>
    <td align="right">17.25</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.80</td>
    <td align="right">16.25</td>
    <td align="right">16.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.59</td>
    <td align="right">9.08</td>
    <td align="right">12.38</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.10</td>
    <td align="right">10.45</td>
    <td align="right">14.43</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">22.48</td>
    <td align="right">22.47</td>
    <td align="right">22.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.90</td>
    <td align="right">11.71</td>
    <td align="right">13.01</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.06</td>
    <td align="right">15.46</td>
    <td align="right">15.34</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.32</td>
    <td align="right">26.68</td>
    <td align="right">27.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">19.99</td>
    <td align="right">28.04</td>
    <td align="right">20.00</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">29.27</td>
    <td align="right">27.24</td>
    <td align="right">18.57</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">38.54</td>
    <td align="right">34.90</td>
    <td align="right">34.25</td>
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
    <td align="right">26.68</td>
    <td align="right">6.31</td>
    <td align="right">5.08</td>
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
    <td align="right">8.82</td>
    <td align="right">5.92</td>
    <td align="right">15.07</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="right">1.78</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.27</td>
    <td align="right">1.76</td>
    <td align="right">1.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.02</td>
    <td align="right">7.67</td>
    <td align="right">13.64</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">2.12</td>
    <td align="right">1.54</td>
    <td align="right">1.85</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.85</td>
    <td align="right">1.84</td>
    <td align="right">1.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.38</td>
    <td align="right">8.81</td>
    <td align="right">11.74</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.78</td>
    <td align="right">1.81</td>
    <td align="right">1.86</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.02</td>
    <td align="right">1.85</td>
    <td align="right">1.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">17.98</td>
    <td align="right">11.36</td>
    <td align="right">12.28</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.88</td>
    <td align="right">2.10</td>
    <td align="right">2.08</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.94</td>
    <td align="right">1.82</td>
    <td align="right">1.61</td>
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
    <td align="right">2.32</td>
    <td align="right">1.85</td>
    <td align="right">1.83</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.50</td>
    <td align="right">1.89</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.14</td>
    <td align="right">1.86</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.42</td>
    <td align="right">2.13</td>
    <td align="right">2.05</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.06</td>
    <td align="right">2.43</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.62</td>
    <td align="right">1.50</td>
    <td align="right">1.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.49</td>
    <td align="right">3.16</td>
    <td align="right">3.21</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.49</td>
    <td align="right">3.21</td>
    <td align="right">3.15</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.08</td>
    <td align="right">2.64</td>
    <td align="right">2.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.70</td>
    <td align="right">3.49</td>
    <td align="right">3.47</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.86</td>
    <td align="right">3.89</td>
    <td align="right">5.32</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.37</td>
    <td align="right">3.69</td>
    <td align="right">1.96</td>
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
    <td align="right">2.11</td>
    <td align="right">2.75</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.46</td>
    <td align="right">1.79</td>
    <td align="right">1.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.31</td>
    <td align="right">2.00</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.23</td>
    <td align="right">1.73</td>
    <td align="right">1.68</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.52</td>
    <td align="right">2.42</td>
    <td align="right">2.31</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.95</td>
    <td align="right">2.29</td>
    <td align="right">2.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.35</td>
    <td align="right">3.05</td>
    <td align="right">1.95</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.23</td>
    <td align="right">2.99</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.55</td>
    <td align="right">3.32</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.26</td>
    <td align="right">3.33</td>
    <td align="right">1.90</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.03</td>
    <td align="right">3.86</td>
    <td align="right">3.80</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.33</td>
    <td align="right">4.29</td>
    <td align="right">4.56</td>
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
    <td align="right">3.54</td>
    <td align="right">3.48</td>
    <td align="right">11.28</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.90</td>
    <td align="right">4.36</td>
    <td align="right">14.00</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">8.24</td>
    <td align="right">5.43</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.28</td>
    <td align="right">4.95</td>
    <td align="right">11.25</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">8.65</td>
    <td align="right">5.18</td>
    <td align="right">11.64</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">11.78</td>
    <td align="right">8.15</td>
    <td align="right">7.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.47</td>
    <td align="right">6.44</td>
    <td align="right">11.02</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">10.04</td>
    <td align="right">6.80</td>
    <td align="right">12.16</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.98</td>
    <td align="right">8.12</td>
    <td align="right">12.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">8.84</td>
    <td align="right">7.49</td>
    <td align="right">11.61</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">9.97</td>
    <td align="right">7.60</td>
    <td align="right">11.99</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">18.27</td>
    <td align="right">11.73</td>
    <td align="right">11.70</td>
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
    <td align="right">26.49</td>
    <td align="right">13.10</td>
    <td align="right">8.61</td>
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
    <td align="right">9.21</td>
    <td align="right">8.84</td>
    <td align="right">18.01</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.99</td>
    <td align="right">3.75</td>
    <td align="right">3.92</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.42</td>
    <td align="right">2.27</td>
    <td align="right">3.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">24.32</td>
    <td align="right">17.63</td>
    <td align="right">21.22</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.92</td>
    <td align="right">5.74</td>
    <td align="right">6.28</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.29</td>
    <td align="right">6.37</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">44.37</td>
    <td align="right">37.35</td>
    <td align="right">23.31</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.52</td>
    <td align="right">9.02</td>
    <td align="right">8.79</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.70</td>
    <td align="right">8.38</td>
    <td align="right">8.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">70.74</td>
    <td align="right">63.29</td>
    <td align="right">23.07</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.34</td>
    <td align="right">9.99</td>
    <td align="right">10.19</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.99</td>
    <td align="right">8.47</td>
    <td align="right">8.03</td>
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
    <td align="right">3.69</td>
    <td align="right">4.02</td>
    <td align="right">3.91</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.88</td>
    <td align="right">3.68</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.96</td>
    <td align="right">3.19</td>
    <td align="right">3.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.97</td>
    <td align="right">7.63</td>
    <td align="right">7.36</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.41</td>
    <td align="right">7.90</td>
    <td align="right">8.75</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.31</td>
    <td align="right">5.22</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">13.33</td>
    <td align="right">10.83</td>
    <td align="right">14.26</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">16.17</td>
    <td align="right">13.20</td>
    <td align="right">13.09</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.98</td>
    <td align="right">8.00</td>
    <td align="right">6.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">20.16</td>
    <td align="right">16.78</td>
    <td align="right">17.69</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.98</td>
    <td align="right">19.06</td>
    <td align="right">19.46</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.71</td>
    <td align="right">13.99</td>
    <td align="right">6.85</td>
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
    <td align="right">2.45</td>
    <td align="right">2.43</td>
    <td align="right">2.51</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.70</td>
    <td align="right">2.44</td>
    <td align="right">2.41</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.67</td>
    <td align="right">2.65</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.81</td>
    <td align="right">3.00</td>
    <td align="right">3.01</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.85</td>
    <td align="right">4.52</td>
    <td align="right">4.14</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.07</td>
    <td align="right">6.65</td>
    <td align="right">5.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.15</td>
    <td align="right">7.72</td>
    <td align="right">5.07</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.71</td>
    <td align="right">9.03</td>
    <td align="right">8.95</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">9.61</td>
    <td align="right">8.67</td>
    <td align="right">8.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">13.79</td>
    <td align="right">14.61</td>
    <td align="right">8.43</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.66</td>
    <td align="right">12.38</td>
    <td align="right">12.35</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.72</td>
    <td align="right">13.27</td>
    <td align="right">13.26</td>
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
    <td align="right">4.42</td>
    <td align="right">4.10</td>
    <td align="right">11.11</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.52</td>
    <td align="right">4.90</td>
    <td align="right">13.94</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">8.66</td>
    <td align="right">6.41</td>
    <td align="right">6.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.23</td>
    <td align="right">7.23</td>
    <td align="right">12.02</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.33</td>
    <td align="right">7.27</td>
    <td align="right">12.47</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">13.41</td>
    <td align="right">14.52</td>
    <td align="right">11.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">17.85</td>
    <td align="right">12.14</td>
    <td align="right">13.37</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.23</td>
    <td align="right">14.32</td>
    <td align="right">16.73</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">22.12</td>
    <td align="right">20.88</td>
    <td align="right">20.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">24.24</td>
    <td align="right">20.07</td>
    <td align="right">15.75</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">27.71</td>
    <td align="right">19.29</td>
    <td align="right">16.51</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.55</td>
    <td align="right">36.02</td>
    <td align="right">38.75</td>
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
    <td align="right">35.52</td>
    <td align="right">5.58</td>
    <td align="right">3.48</td>
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
    <td align="right">11.91</td>
    <td align="right">12.41</td>
    <td align="right">16.85</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.81</td>
    <td align="right">4.20</td>
    <td align="right">4.21</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.91</td>
    <td align="right">5.22</td>
    <td align="right">5.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.23</td>
    <td align="right">17.59</td>
    <td align="right">17.56</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.95</td>
    <td align="right">4.96</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">7.99</td>
    <td align="right">5.92</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.50</td>
    <td align="right">21.04</td>
    <td align="right">16.51</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.60</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.26</td>
    <td align="right">6.45</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.79</td>
    <td align="right">27.17</td>
    <td align="right">17.24</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.08</td>
    <td align="right">5.87</td>
    <td align="right">5.89</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.42</td>
    <td align="right">7.59</td>
    <td align="right">7.50</td>
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
    <td align="right">7.85</td>
    <td align="right">5.53</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">11.70</td>
    <td align="right">5.53</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.38</td>
    <td align="right">3.95</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.09</td>
    <td align="right">8.20</td>
    <td align="right">8.17</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.24</td>
    <td align="right">8.67</td>
    <td align="right">8.64</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.89</td>
    <td align="right">4.87</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.45</td>
    <td align="right">10.75</td>
    <td align="right">10.88</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.85</td>
    <td align="right">10.48</td>
    <td align="right">10.47</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.91</td>
    <td align="right">7.00</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.47</td>
    <td align="right">14.19</td>
    <td align="right">14.22</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.65</td>
    <td align="right">13.45</td>
    <td align="right">12.62</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.06</td>
    <td align="right">7.15</td>
    <td align="right">5.31</td>
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
    <td align="right">3.78</td>
    <td align="right">3.84</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.49</td>
    <td align="right">5.49</td>
    <td align="right">5.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.73</td>
    <td align="right">5.39</td>
    <td align="right">5.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.23</td>
    <td align="right">5.58</td>
    <td align="right">4.70</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.75</td>
    <td align="right">5.85</td>
    <td align="right">5.03</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.96</td>
    <td align="right">7.00</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.09</td>
    <td align="right">6.77</td>
    <td align="right">5.00</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.69</td>
    <td align="right">9.17</td>
    <td align="right">7.43</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">10.02</td>
    <td align="right">9.29</td>
    <td align="right">7.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.14</td>
    <td align="right">6.99</td>
    <td align="right">5.15</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.15</td>
    <td align="right">10.51</td>
    <td align="right">7.57</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.25</td>
    <td align="right">10.49</td>
    <td align="right">7.55</td>
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
    <td align="right">8.88</td>
    <td align="right">8.60</td>
    <td align="right">13.70</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.04</td>
    <td align="right">11.66</td>
    <td align="right">17.10</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.88</td>
    <td align="right">12.01</td>
    <td align="right">12.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.96</td>
    <td align="right">11.80</td>
    <td align="right">14.46</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">14.11</td>
    <td align="right">13.59</td>
    <td align="right">16.13</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">19.53</td>
    <td align="right">18.37</td>
    <td align="right">16.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.26</td>
    <td align="right">14.57</td>
    <td align="right">14.36</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">18.52</td>
    <td align="right">17.23</td>
    <td align="right">15.47</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">21.41</td>
    <td align="right">18.55</td>
    <td align="right">19.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">18.86</td>
    <td align="right">17.28</td>
    <td align="right">15.32</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.24</td>
    <td align="right">20.41</td>
    <td align="right">15.01</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">31.14</td>
    <td align="right">28.74</td>
    <td align="right">26.94</td>
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
    <td align="right">39.53</td>
    <td align="right">20.95</td>
    <td align="right">7.08</td>
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
    <td align="right">14.39</td>
    <td align="right">12.96</td>
    <td align="right">17.57</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.04</td>
    <td align="right">4.45</td>
    <td align="right">4.45</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.89</td>
    <td align="right">5.55</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.00</td>
    <td align="right">18.62</td>
    <td align="right">18.30</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.56</td>
    <td align="right">5.11</td>
    <td align="right">5.10</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.23</td>
    <td align="right">6.32</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.33</td>
    <td align="right">24.91</td>
    <td align="right">17.28</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.12</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.14</td>
    <td align="right">7.78</td>
    <td align="right">7.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">41.24</td>
    <td align="right">36.56</td>
    <td align="right">18.55</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.39</td>
    <td align="right">7.42</td>
    <td align="right">7.26</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.95</td>
    <td align="right">9.12</td>
    <td align="right">9.12</td>
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
    <td align="right">9.29</td>
    <td align="right">6.21</td>
    <td align="right">6.19</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.41</td>
    <td align="right">6.26</td>
    <td align="right">6.28</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.82</td>
    <td align="right">4.14</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.37</td>
    <td align="right">9.73</td>
    <td align="right">9.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.19</td>
    <td align="right">9.24</td>
    <td align="right">9.19</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.46</td>
    <td align="right">5.27</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.18</td>
    <td align="right">12.61</td>
    <td align="right">12.79</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">16.87</td>
    <td align="right">11.53</td>
    <td align="right">11.41</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.72</td>
    <td align="right">7.80</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">20.89</td>
    <td align="right">17.61</td>
    <td align="right">17.70</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.20</td>
    <td align="right">15.63</td>
    <td align="right">14.60</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">8.04</td>
    <td align="right">10.37</td>
    <td align="right">8.20</td>
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
    <td align="right">3.67</td>
    <td align="right">4.08</td>
    <td align="right">4.06</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.86</td>
    <td align="right">5.78</td>
    <td align="right">5.78</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.25</td>
    <td align="right">5.71</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.72</td>
    <td align="right">5.94</td>
    <td align="right">5.00</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.40</td>
    <td align="right">6.34</td>
    <td align="right">5.44</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.69</td>
    <td align="right">7.45</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.83</td>
    <td align="right">7.40</td>
    <td align="right">5.52</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.95</td>
    <td align="right">10.21</td>
    <td align="right">8.44</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.90</td>
    <td align="right">10.18</td>
    <td align="right">8.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.11</td>
    <td align="right">11.63</td>
    <td align="right">8.90</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.22</td>
    <td align="right">12.53</td>
    <td align="right">9.17</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.78</td>
    <td align="right">13.69</td>
    <td align="right">10.31</td>
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
    <td align="right">9.96</td>
    <td align="right">9.54</td>
    <td align="right">13.95</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.73</td>
    <td align="right">12.54</td>
    <td align="right">17.59</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.09</td>
    <td align="right">15.08</td>
    <td align="right">15.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.74</td>
    <td align="right">12.49</td>
    <td align="right">14.84</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.72</td>
    <td align="right">14.66</td>
    <td align="right">16.56</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">23.09</td>
    <td align="right">22.86</td>
    <td align="right">21.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.97</td>
    <td align="right">15.96</td>
    <td align="right">14.92</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">19.92</td>
    <td align="right">19.15</td>
    <td align="right">15.99</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.45</td>
    <td align="right">22.42</td>
    <td align="right">22.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.36</td>
    <td align="right">21.11</td>
    <td align="right">17.05</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">25.89</td>
    <td align="right">23.99</td>
    <td align="right">16.02</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">36.67</td>
    <td align="right">34.53</td>
    <td align="right">34.03</td>
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
    <td align="right">61.59</td>
    <td align="right">30.15</td>
    <td align="right">14.17</td>
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
    <td align="right">27.43</td>
    <td align="right">42.13</td>
    <td align="right">36.55</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.51</td>
    <td align="right">15.69</td>
    <td align="right">15.57</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.23</td>
    <td align="right">19.16</td>
    <td align="right">19.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.16</td>
    <td align="right">60.51</td>
    <td align="right">37.73</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.38</td>
    <td align="right">19.58</td>
    <td align="right">19.57</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.28</td>
    <td align="right">18.64</td>
    <td align="right">18.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.03</td>
    <td align="right">78.47</td>
    <td align="right">38.36</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.43</td>
    <td align="right">18.56</td>
    <td align="right">18.46</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.23</td>
    <td align="right">18.31</td>
    <td align="right">18.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.40</td>
    <td align="right">97.84</td>
    <td align="right">38.12</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.25</td>
    <td align="right">18.77</td>
    <td align="right">18.79</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.17</td>
    <td align="right">20.07</td>
    <td align="right">19.99</td>
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
    <td align="right">16.28</td>
    <td align="right">21.22</td>
    <td align="right">21.28</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.82</td>
    <td align="right">22.20</td>
    <td align="right">22.24</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.04</td>
    <td align="right">13.65</td>
    <td align="right">13.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.37</td>
    <td align="right">26.09</td>
    <td align="right">26.08</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.90</td>
    <td align="right">27.84</td>
    <td align="right">27.95</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.00</td>
    <td align="right">15.89</td>
    <td align="right">15.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.35</td>
    <td align="right">33.06</td>
    <td align="right">33.03</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.75</td>
    <td align="right">46.67</td>
    <td align="right">46.68</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.03</td>
    <td align="right">19.60</td>
    <td align="right">19.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.55</td>
    <td align="right">36.29</td>
    <td align="right">36.23</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.74</td>
    <td align="right">56.52</td>
    <td align="right">56.54</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.53</td>
    <td align="right">25.65</td>
    <td align="right">25.58</td>
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
    <td align="right">15.61</td>
    <td align="right">15.64</td>
    <td align="right">15.64</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.27</td>
    <td align="right">21.21</td>
    <td align="right">21.23</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.79</td>
    <td align="right">22.24</td>
    <td align="right">22.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.14</td>
    <td align="right">20.47</td>
    <td align="right">20.49</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.40</td>
    <td align="right">26.08</td>
    <td align="right">26.11</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.86</td>
    <td align="right">27.85</td>
    <td align="right">27.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.59</td>
    <td align="right">24.87</td>
    <td align="right">24.84</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.34</td>
    <td align="right">33.08</td>
    <td align="right">33.07</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.86</td>
    <td align="right">46.73</td>
    <td align="right">46.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.59</td>
    <td align="right">37.50</td>
    <td align="right">37.45</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.52</td>
    <td align="right">36.22</td>
    <td align="right">36.22</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.75</td>
    <td align="right">56.51</td>
    <td align="right">56.53</td>
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
    <td align="right">20.84</td>
    <td align="right">25.48</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.41</td>
    <td align="right">29.14</td>
    <td align="right">34.49</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.63</td>
    <td align="right">30.32</td>
    <td align="right">30.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.48</td>
    <td align="right">28.17</td>
    <td align="right">25.87</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.77</td>
    <td align="right">34.17</td>
    <td align="right">32.67</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">38.24</td>
    <td align="right">38.37</td>
    <td align="right">38.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.59</td>
    <td align="right">33.97</td>
    <td align="right">25.99</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">47.20</td>
    <td align="right">42.05</td>
    <td align="right">34.03</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">40.06</td>
    <td align="right">41.96</td>
    <td align="right">41.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.75</td>
    <td align="right">40.40</td>
    <td align="right">27.08</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">48.88</td>
    <td align="right">44.06</td>
    <td align="right">31.66</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">54.89</td>
    <td align="right">58.84</td>
    <td align="right">59.05</td>
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
    <td align="right">69.76</td>
    <td align="right">104.91</td>
    <td align="right">20.50</td>
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
    <td align="right">28.31</td>
    <td align="right">44.51</td>
    <td align="right">40.66</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.28</td>
    <td align="right">16.29</td>
    <td align="right">15.92</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.65</td>
    <td align="right">19.23</td>
    <td align="right">19.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.83</td>
    <td align="right">64.39</td>
    <td align="right">40.83</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.44</td>
    <td align="right">20.22</td>
    <td align="right">21.49</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.95</td>
    <td align="right">18.95</td>
    <td align="right">19.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">64.43</td>
    <td align="right">110.03</td>
    <td align="right">52.47</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">33.17</td>
    <td align="right">29.01</td>
    <td align="right">30.53</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">20.39</td>
    <td align="right">22.67</td>
    <td align="right">19.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">105.97</td>
    <td align="right">160.00</td>
    <td align="right">63.74</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">50.09</td>
    <td align="right">52.97</td>
    <td align="right">53.11</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">55.43</td>
    <td align="right">56.73</td>
    <td align="right">57.80</td>
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
    <td align="right">20.99</td>
    <td align="right">32.40</td>
    <td align="right">26.71</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">47.96</td>
    <td align="right">33.46</td>
    <td align="right">33.47</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">15.94</td>
    <td align="right">18.16</td>
    <td align="right">15.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.83</td>
    <td align="right">44.48</td>
    <td align="right">33.39</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">57.66</td>
    <td align="right">38.86</td>
    <td align="right">41.08</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">17.60</td>
    <td align="right">18.45</td>
    <td align="right">17.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">51.69</td>
    <td align="right">36.56</td>
    <td align="right">46.96</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">74.31</td>
    <td align="right">64.67</td>
    <td align="right">63.08</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">31.60</td>
    <td align="right">39.07</td>
    <td align="right">36.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">83.33</td>
    <td align="right">83.36</td>
    <td align="right">96.05</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">111.21</td>
    <td align="right">77.55</td>
    <td align="right">85.07</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">56.08</td>
    <td align="right">39.39</td>
    <td align="right">52.92</td>
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
    <td align="right">16.32</td>
    <td align="right">16.30</td>
    <td align="right">16.32</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.88</td>
    <td align="right">22.19</td>
    <td align="right">22.23</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.98</td>
    <td align="right">23.31</td>
    <td align="right">23.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.77</td>
    <td align="right">20.13</td>
    <td align="right">20.19</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.17</td>
    <td align="right">25.67</td>
    <td align="right">25.65</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.69</td>
    <td align="right">28.26</td>
    <td align="right">28.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">28.22</td>
    <td align="right">24.66</td>
    <td align="right">24.93</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">33.93</td>
    <td align="right">40.18</td>
    <td align="right">38.55</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">68.88</td>
    <td align="right">56.82</td>
    <td align="right">65.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">43.58</td>
    <td align="right">62.94</td>
    <td align="right">55.01</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">68.71</td>
    <td align="right">89.34</td>
    <td align="right">105.79</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">128.01</td>
    <td align="right">92.91</td>
    <td align="right">101.30</td>
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
    <td align="right">18.49</td>
    <td align="right">22.37</td>
    <td align="right">26.96</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">40.09</td>
    <td align="right">34.07</td>
    <td align="right">40.57</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.82</td>
    <td align="right">33.13</td>
    <td align="right">33.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">37.60</td>
    <td align="right">43.84</td>
    <td align="right">34.12</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">111.22</td>
    <td align="right">101.41</td>
    <td align="right">68.10</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">43.15</td>
    <td align="right">43.44</td>
    <td align="right">41.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">77.09</td>
    <td align="right">73.89</td>
    <td align="right">40.34</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">126.87</td>
    <td align="right">118.56</td>
    <td align="right">67.76</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">47.80</td>
    <td align="right">50.28</td>
    <td align="right">49.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">102.81</td>
    <td align="right">94.39</td>
    <td align="right">46.02</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">105.70</td>
    <td align="right">120.10</td>
    <td align="right">66.59</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">72.54</td>
    <td align="right">92.59</td>
    <td align="right">88.10</td>
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
    <td align="right">60.44</td>
    <td align="right">10.32</td>
    <td align="right">7.44</td>
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
    <td align="right">13.85</td>
    <td align="right">22.74</td>
    <td align="right">26.58</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.54</td>
    <td align="right">12.32</td>
    <td align="right">12.33</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.72</td>
    <td align="right">13.83</td>
    <td align="right">13.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.32</td>
    <td align="right">34.81</td>
    <td align="right">28.70</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.02</td>
    <td align="right">14.08</td>
    <td align="right">14.06</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.51</td>
    <td align="right">15.28</td>
    <td align="right">15.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.93</td>
    <td align="right">47.32</td>
    <td align="right">30.20</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.82</td>
    <td align="right">16.30</td>
    <td align="right">15.43</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.56</td>
    <td align="right">16.66</td>
    <td align="right">16.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.17</td>
    <td align="right">60.19</td>
    <td align="right">30.62</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.48</td>
    <td align="right">16.25</td>
    <td align="right">16.28</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.83</td>
    <td align="right">17.82</td>
    <td align="right">17.84</td>
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
    <td align="right">12.63</td>
    <td align="right">16.04</td>
    <td align="right">16.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.65</td>
    <td align="right">16.65</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.09</td>
    <td align="right">9.31</td>
    <td align="right">9.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.32</td>
    <td align="right">22.47</td>
    <td align="right">22.48</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.24</td>
    <td align="right">22.31</td>
    <td align="right">22.28</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.06</td>
    <td align="right">13.93</td>
    <td align="right">13.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.94</td>
    <td align="right">32.15</td>
    <td align="right">32.06</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.45</td>
    <td align="right">30.56</td>
    <td align="right">30.52</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.63</td>
    <td align="right">17.53</td>
    <td align="right">17.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.81</td>
    <td align="right">35.60</td>
    <td align="right">35.65</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.88</td>
    <td align="right">35.74</td>
    <td align="right">35.73</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.28</td>
    <td align="right">20.46</td>
    <td align="right">20.45</td>
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
    <td align="right">6.52</td>
    <td align="right">9.35</td>
    <td align="right">9.36</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.63</td>
    <td align="right">16.05</td>
    <td align="right">16.06</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.22</td>
    <td align="right">16.65</td>
    <td align="right">16.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.37</td>
    <td align="right">13.66</td>
    <td align="right">13.65</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.35</td>
    <td align="right">22.44</td>
    <td align="right">22.45</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.28</td>
    <td align="right">22.25</td>
    <td align="right">22.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.47</td>
    <td align="right">17.58</td>
    <td align="right">17.59</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.02</td>
    <td align="right">32.09</td>
    <td align="right">32.04</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.55</td>
    <td align="right">30.53</td>
    <td align="right">30.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">15.99</td>
    <td align="right">21.03</td>
    <td align="right">20.95</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.89</td>
    <td align="right">35.64</td>
    <td align="right">35.63</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.93</td>
    <td align="right">35.69</td>
    <td align="right">35.76</td>
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
    <td align="right">12.95</td>
    <td align="right">16.62</td>
    <td align="right">19.88</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">49.01</td>
    <td align="right">33.04</td>
    <td align="right">36.67</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.78</td>
    <td align="right">23.97</td>
    <td align="right">23.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.84</td>
    <td align="right">23.50</td>
    <td align="right">20.63</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.62</td>
    <td align="right">37.77</td>
    <td align="right">36.00</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.07</td>
    <td align="right">31.93</td>
    <td align="right">31.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">23.90</td>
    <td align="right">30.05</td>
    <td align="right">20.25</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.86</td>
    <td align="right">44.38</td>
    <td align="right">36.35</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">29.95</td>
    <td align="right">35.16</td>
    <td align="right">35.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">29.78</td>
    <td align="right">38.31</td>
    <td align="right">25.04</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">65.53</td>
    <td align="right">51.33</td>
    <td align="right">39.33</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">41.73</td>
    <td align="right">45.67</td>
    <td align="right">45.54</td>
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
    <td align="right">76.75</td>
    <td align="right">46.84</td>
    <td align="right">10.73</td>
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
    <td align="right">14.00</td>
    <td align="right">22.79</td>
    <td align="right">28.25</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.67</td>
    <td align="right">12.53</td>
    <td align="right">12.51</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.88</td>
    <td align="right">13.97</td>
    <td align="right">13.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.52</td>
    <td align="right">34.53</td>
    <td align="right">29.41</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.98</td>
    <td align="right">13.93</td>
    <td align="right">13.90</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.40</td>
    <td align="right">15.10</td>
    <td align="right">15.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.98</td>
    <td align="right">47.59</td>
    <td align="right">30.66</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.72</td>
    <td align="right">15.19</td>
    <td align="right">15.20</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.42</td>
    <td align="right">16.47</td>
    <td align="right">16.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">31.75</td>
    <td align="right">62.35</td>
    <td align="right">31.56</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.86</td>
    <td align="right">16.35</td>
    <td align="right">16.58</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">16.17</td>
    <td align="right">18.57</td>
    <td align="right">19.08</td>
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
    <td align="right">13.10</td>
    <td align="right">16.62</td>
    <td align="right">16.64</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.32</td>
    <td align="right">17.57</td>
    <td align="right">17.56</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.26</td>
    <td align="right">9.44</td>
    <td align="right">9.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.00</td>
    <td align="right">21.98</td>
    <td align="right">22.03</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.41</td>
    <td align="right">22.08</td>
    <td align="right">22.16</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.42</td>
    <td align="right">14.03</td>
    <td align="right">14.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.04</td>
    <td align="right">33.16</td>
    <td align="right">33.36</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.04</td>
    <td align="right">31.37</td>
    <td align="right">31.58</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.27</td>
    <td align="right">16.87</td>
    <td align="right">17.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">28.83</td>
    <td align="right">37.78</td>
    <td align="right">37.26</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.37</td>
    <td align="right">36.16</td>
    <td align="right">37.47</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">16.64</td>
    <td align="right">21.13</td>
    <td align="right">21.88</td>
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
    <td align="right">6.74</td>
    <td align="right">9.54</td>
    <td align="right">9.55</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.02</td>
    <td align="right">16.62</td>
    <td align="right">16.60</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.32</td>
    <td align="right">17.57</td>
    <td align="right">17.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.57</td>
    <td align="right">13.44</td>
    <td align="right">13.44</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.95</td>
    <td align="right">22.04</td>
    <td align="right">22.05</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.51</td>
    <td align="right">22.21</td>
    <td align="right">22.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">12.52</td>
    <td align="right">17.08</td>
    <td align="right">17.01</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.09</td>
    <td align="right">33.95</td>
    <td align="right">33.15</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.36</td>
    <td align="right">31.33</td>
    <td align="right">31.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">16.68</td>
    <td align="right">21.30</td>
    <td align="right">21.58</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">27.41</td>
    <td align="right">37.58</td>
    <td align="right">37.04</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">34.75</td>
    <td align="right">38.24</td>
    <td align="right">37.11</td>
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
    <td align="right">13.13</td>
    <td align="right">16.60</td>
    <td align="right">20.34</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.14</td>
    <td align="right">34.09</td>
    <td align="right">37.35</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">22.32</td>
    <td align="right">25.97</td>
    <td align="right">25.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.16</td>
    <td align="right">23.60</td>
    <td align="right">20.71</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">55.23</td>
    <td align="right">38.12</td>
    <td align="right">36.40</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">28.84</td>
    <td align="right">33.62</td>
    <td align="right">33.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">24.85</td>
    <td align="right">31.11</td>
    <td align="right">20.50</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">73.67</td>
    <td align="right">57.49</td>
    <td align="right">45.82</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">32.20</td>
    <td align="right">36.53</td>
    <td align="right">36.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">49.23</td>
    <td align="right">57.84</td>
    <td align="right">31.31</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">115.31</td>
    <td align="right">97.37</td>
    <td align="right">71.56</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">59.65</td>
    <td align="right">58.35</td>
    <td align="right">65.36</td>
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
    <td align="right">43.67</td>
    <td align="right">8.69</td>
    <td align="right">6.57</td>
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
    <td align="right">58.99</td>
    <td align="right">54.86</td>
    <td align="right">41.73</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.80</td>
    <td align="right">20.50</td>
    <td align="right">24.46</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.04</td>
    <td align="right">26.14</td>
    <td align="right">29.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.64</td>
    <td align="right">80.48</td>
    <td align="right">43.91</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">24.05</td>
    <td align="right">22.00</td>
    <td align="right">24.20</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">26.87</td>
    <td align="right">28.38</td>
    <td align="right">30.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.60</td>
    <td align="right">97.85</td>
    <td align="right">43.38</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.74</td>
    <td align="right">22.86</td>
    <td align="right">24.41</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.58</td>
    <td align="right">30.89</td>
    <td align="right">32.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">140.55</td>
    <td align="right">123.76</td>
    <td align="right">45.25</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.30</td>
    <td align="right">24.22</td>
    <td align="right">25.19</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.06</td>
    <td align="right">33.47</td>
    <td align="right">34.31</td>
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
    <td align="right">23.47</td>
    <td align="right">43.22</td>
    <td align="right">43.82</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.25</td>
    <td align="right">43.09</td>
    <td align="right">43.19</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.74</td>
    <td align="right">24.96</td>
    <td align="right">24.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.51</td>
    <td align="right">58.32</td>
    <td align="right">58.97</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.72</td>
    <td align="right">59.68</td>
    <td align="right">59.11</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.50</td>
    <td align="right">36.55</td>
    <td align="right">25.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">39.85</td>
    <td align="right">79.75</td>
    <td align="right">80.66</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.87</td>
    <td align="right">81.44</td>
    <td align="right">80.81</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.13</td>
    <td align="right">55.31</td>
    <td align="right">39.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.07</td>
    <td align="right">88.57</td>
    <td align="right">88.79</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.59</td>
    <td align="right">95.72</td>
    <td align="right">95.65</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.36</td>
    <td align="right">55.94</td>
    <td align="right">40.86</td>
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
    <td align="right">18.68</td>
    <td align="right">26.41</td>
    <td align="right">26.20</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.70</td>
    <td align="right">28.97</td>
    <td align="right">29.27</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.99</td>
    <td align="right">31.05</td>
    <td align="right">31.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.22</td>
    <td align="right">47.07</td>
    <td align="right">34.94</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.50</td>
    <td align="right">39.28</td>
    <td align="right">27.67</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.11</td>
    <td align="right">52.37</td>
    <td align="right">40.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.65</td>
    <td align="right">54.47</td>
    <td align="right">39.58</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.90</td>
    <td align="right">53.43</td>
    <td align="right">34.74</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.18</td>
    <td align="right">61.53</td>
    <td align="right">43.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.89</td>
    <td align="right">55.63</td>
    <td align="right">39.06</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.71</td>
    <td align="right">64.62</td>
    <td align="right">44.38</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.31</td>
    <td align="right">64.21</td>
    <td align="right">45.03</td>
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
    <td align="right">25.42</td>
    <td align="right">43.79</td>
    <td align="right">36.05</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.93</td>
    <td align="right">55.77</td>
    <td align="right">41.78</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">37.01</td>
    <td align="right">62.56</td>
    <td align="right">62.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.88</td>
    <td align="right">61.29</td>
    <td align="right">37.03</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.96</td>
    <td align="right">64.29</td>
    <td align="right">39.84</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">46.06</td>
    <td align="right">81.29</td>
    <td align="right">81.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">41.19</td>
    <td align="right">73.42</td>
    <td align="right">36.97</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.59</td>
    <td align="right">80.64</td>
    <td align="right">41.84</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.40</td>
    <td align="right">87.75</td>
    <td align="right">88.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">51.96</td>
    <td align="right">94.16</td>
    <td align="right">38.56</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.80</td>
    <td align="right">97.86</td>
    <td align="right">41.29</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">67.07</td>
    <td align="right">125.25</td>
    <td align="right">124.92</td>
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
    <td align="right">63.63</td>
    <td align="right">35.76</td>
    <td align="right">11.45</td>
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
    <td align="right">67.22</td>
    <td align="right">60.62</td>
    <td align="right">46.74</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.28</td>
    <td align="right">21.89</td>
    <td align="right">26.88</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">28.19</td>
    <td align="right">29.25</td>
    <td align="right">33.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">101.67</td>
    <td align="right">86.87</td>
    <td align="right">48.06</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">26.45</td>
    <td align="right">23.04</td>
    <td align="right">26.83</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">31.66</td>
    <td align="right">33.20</td>
    <td align="right">41.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">141.72</td>
    <td align="right">121.67</td>
    <td align="right">49.31</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">31.70</td>
    <td align="right">26.71</td>
    <td align="right">28.64</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">38.49</td>
    <td align="right">38.28</td>
    <td align="right">39.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">220.19</td>
    <td align="right">214.52</td>
    <td align="right">62.97</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">56.39</td>
    <td align="right">42.29</td>
    <td align="right">45.02</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">59.42</td>
    <td align="right">49.56</td>
    <td align="right">53.55</td>
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
    <td align="right">25.61</td>
    <td align="right">47.91</td>
    <td align="right">46.96</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.33</td>
    <td align="right">44.43</td>
    <td align="right">44.76</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.09</td>
    <td align="right">31.18</td>
    <td align="right">30.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">33.17</td>
    <td align="right">64.69</td>
    <td align="right">63.59</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.12</td>
    <td align="right">68.36</td>
    <td align="right">68.22</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.60</td>
    <td align="right">44.63</td>
    <td align="right">30.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">44.99</td>
    <td align="right">87.45</td>
    <td align="right">87.22</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">52.41</td>
    <td align="right">88.05</td>
    <td align="right">90.49</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">41.87</td>
    <td align="right">82.97</td>
    <td align="right">60.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">58.75</td>
    <td align="right">103.31</td>
    <td align="right">102.12</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">66.12</td>
    <td align="right">115.83</td>
    <td align="right">114.50</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">55.47</td>
    <td align="right">103.66</td>
    <td align="right">81.75</td>
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
    <td align="right">21.15</td>
    <td align="right">40.84</td>
    <td align="right">40.84</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.85</td>
    <td align="right">37.25</td>
    <td align="right">34.38</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">22.60</td>
    <td align="right">41.34</td>
    <td align="right">37.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">24.29</td>
    <td align="right">74.83</td>
    <td align="right">55.95</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">21.28</td>
    <td align="right">52.40</td>
    <td align="right">35.18</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">23.34</td>
    <td align="right">70.86</td>
    <td align="right">62.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">83.21</td>
    <td align="right">91.25</td>
    <td align="right">88.70</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">45.06</td>
    <td align="right">93.12</td>
    <td align="right">55.64</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">43.58</td>
    <td align="right">83.86</td>
    <td align="right">58.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">77.25</td>
    <td align="right">110.89</td>
    <td align="right">89.72</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">67.38</td>
    <td align="right">123.11</td>
    <td align="right">61.07</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">43.83</td>
    <td align="right">85.11</td>
    <td align="right">68.97</td>
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
    <td align="right">28.24</td>
    <td align="right">45.05</td>
    <td align="right">39.93</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">37.36</td>
    <td align="right">58.04</td>
    <td align="right">47.13</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">41.59</td>
    <td align="right">63.84</td>
    <td align="right">63.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">44.47</td>
    <td align="right">67.10</td>
    <td align="right">41.79</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">62.34</td>
    <td align="right">73.34</td>
    <td align="right">49.24</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">49.44</td>
    <td align="right">82.62</td>
    <td align="right">82.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">58.75</td>
    <td align="right">94.70</td>
    <td align="right">46.94</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">97.26</td>
    <td align="right">114.34</td>
    <td align="right">55.64</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">55.07</td>
    <td align="right">92.91</td>
    <td align="right">92.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">74.54</td>
    <td align="right">125.10</td>
    <td align="right">54.04</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">100.80</td>
    <td align="right">140.38</td>
    <td align="right">66.17</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">78.69</td>
    <td align="right">137.14</td>
    <td align="right">139.73</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->

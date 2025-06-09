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
    <td align="right">27.19</td>
    <td align="right">6.26</td>
    <td align="right">4.55</td>
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
    <td align="right">12.82</td>
    <td align="right">11.76</td>
    <td align="right">18.04</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.85</td>
    <td align="right">4.59</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.68</td>
    <td align="right">4.96</td>
    <td align="right">4.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.54</td>
    <td align="right">17.21</td>
    <td align="right">18.78</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.41</td>
    <td align="right">5.03</td>
    <td align="right">5.04</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.70</td>
    <td align="right">5.48</td>
    <td align="right">5.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">22.66</td>
    <td align="right">19.82</td>
    <td align="right">17.71</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.00</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.86</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">28.16</td>
    <td align="right">25.03</td>
    <td align="right">18.13</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.60</td>
    <td align="right">5.78</td>
    <td align="right">5.78</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
    <td align="right">6.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1818</td>
    <td align="right">11.08</td>
    <td align="right">12.22</td>
    <td align="right">18.40</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">3.80</td>
    <td align="right">4.63</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.54</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">16.90</td>
    <td align="right">18.08</td>
    <td align="right">19.38</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.28</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">5.23</td>
    <td align="right">5.73</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">19.93</td>
    <td align="right">21.95</td>
    <td align="right">18.58</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">4.80</td>
    <td align="right">5.70</td>
    <td align="right">5.71</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.39</td>
    <td align="right">6.12</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">24.57</td>
    <td align="right">27.67</td>
    <td align="right">18.65</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">5.13</td>
    <td align="right">6.07</td>
    <td align="right">6.07</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">5.90</td>
    <td align="right">6.44</td>
    <td align="right">6.45</td>
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
    <td align="right">5.20</td>
    <td align="right">5.57</td>
    <td align="right">5.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.82</td>
    <td align="right">7.04</td>
    <td align="right">7.02</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.25</td>
    <td align="right">3.49</td>
    <td align="right">3.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.11</td>
    <td align="right">7.75</td>
    <td align="right">7.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.80</td>
    <td align="right">9.49</td>
    <td align="right">9.49</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.57</td>
    <td align="right">3.09</td>
    <td align="right">3.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.13</td>
    <td align="right">11.26</td>
    <td align="right">11.33</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">22.40</td>
    <td align="right">13.50</td>
    <td align="right">13.50</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">6.16</td>
    <td align="right">5.83</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.33</td>
    <td align="right">13.07</td>
    <td align="right">13.01</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.10</td>
    <td align="right">15.93</td>
    <td align="right">15.92</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">6.20</td>
    <td align="right">5.86</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">5.02</td>
    <td align="right">5.67</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">5.91</td>
    <td align="right">6.92</td>
    <td align="right">6.92</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.26</td>
    <td align="right">2.94</td>
    <td align="right">2.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">6.34</td>
    <td align="right">7.91</td>
    <td align="right">7.90</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">7.80</td>
    <td align="right">9.34</td>
    <td align="right">9.35</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.68</td>
    <td align="right">2.74</td>
    <td align="right">2.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">9.79</td>
    <td align="right">11.20</td>
    <td align="right">11.22</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">21.58</td>
    <td align="right">13.67</td>
    <td align="right">13.55</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">6.10</td>
    <td align="right">6.06</td>
    <td align="right">4.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">11.56</td>
    <td align="right">12.98</td>
    <td align="right">12.91</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">12.43</td>
    <td align="right">15.79</td>
    <td align="right">15.87</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">6.15</td>
    <td align="right">6.08</td>
    <td align="right">4.31</td>
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
    <td align="right">3.21</td>
    <td align="right">3.21</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.59</td>
    <td align="right">5.20</td>
    <td align="right">5.19</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.70</td>
    <td align="right">5.02</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.34</td>
    <td align="right">3.32</td>
    <td align="right">3.30</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.43</td>
    <td align="right">4.48</td>
    <td align="right">4.52</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.73</td>
    <td align="right">5.16</td>
    <td align="right">5.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.60</td>
    <td align="right">5.51</td>
    <td align="right">3.94</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.53</td>
    <td align="right">8.11</td>
    <td align="right">6.16</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.92</td>
    <td align="right">7.95</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.64</td>
    <td align="right">5.56</td>
    <td align="right">3.95</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.13</td>
    <td align="right">9.38</td>
    <td align="right">6.31</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.93</td>
    <td align="right">9.05</td>
    <td align="right">6.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4739</td>
    <td align="right">3.23</td>
    <td align="right">2.79</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.65</td>
    <td align="right">4.84</td>
    <td align="right">4.82</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.74</td>
    <td align="right">4.64</td>
    <td align="right">4.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.35</td>
    <td align="right">2.86</td>
    <td align="right">2.87</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.50</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.75</td>
    <td align="right">4.76</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">5.40</td>
    <td align="right">5.66</td>
    <td align="right">3.92</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">8.17</td>
    <td align="right">8.30</td>
    <td align="right">6.31</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">8.59</td>
    <td align="right">7.96</td>
    <td align="right">6.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.46</td>
    <td align="right">5.70</td>
    <td align="right">3.92</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">8.93</td>
    <td align="right">9.58</td>
    <td align="right">6.35</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">9.29</td>
    <td align="right">9.21</td>
    <td align="right">6.22</td>
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
    <td align="right">47.97</td>
    <td align="right">24.25</td>
    <td align="right">15.54</td>
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
    <td align="right">17.85</td>
    <td align="right">15.49</td>
    <td align="right">20.61</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.57</td>
    <td align="right">6.54</td>
    <td align="right">6.33</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.90</td>
    <td align="right">5.77</td>
    <td align="right">5.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">53.82</td>
    <td align="right">52.95</td>
    <td align="right">26.51</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.52</td>
    <td align="right">11.03</td>
    <td align="right">11.02</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">12.43</td>
    <td align="right">12.38</td>
    <td align="right">12.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">86.15</td>
    <td align="right">80.94</td>
    <td align="right">30.69</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.47</td>
    <td align="right">17.99</td>
    <td align="right">17.98</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">18.84</td>
    <td align="right">18.78</td>
    <td align="right">18.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">125.66</td>
    <td align="right">115.22</td>
    <td align="right">36.23</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.78</td>
    <td align="right">21.74</td>
    <td align="right">21.75</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">25.45</td>
    <td align="right">22.55</td>
    <td align="right">22.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1556</td>
    <td align="right">16.06</td>
    <td align="right">17.64</td>
    <td align="right">21.11</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.74</td>
    <td align="right">5.60</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">6.80</td>
    <td align="right">6.95</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">49.09</td>
    <td align="right">53.65</td>
    <td align="right">27.92</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">10.63</td>
    <td align="right">11.66</td>
    <td align="right">11.67</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">12.19</td>
    <td align="right">13.11</td>
    <td align="right">13.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">84.42</td>
    <td align="right">92.02</td>
    <td align="right">33.86</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">16.40</td>
    <td align="right">18.36</td>
    <td align="right">18.35</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">18.79</td>
    <td align="right">19.24</td>
    <td align="right">19.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">124.31</td>
    <td align="right">143.72</td>
    <td align="right">42.09</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">21.40</td>
    <td align="right">21.98</td>
    <td align="right">21.98</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">23.63</td>
    <td align="right">24.19</td>
    <td align="right">24.41</td>
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
    <td align="right">7.14</td>
    <td align="right">7.59</td>
    <td align="right">7.59</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.33</td>
    <td align="right">8.71</td>
    <td align="right">8.66</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.37</td>
    <td align="right">4.90</td>
    <td align="right">4.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.17</td>
    <td align="right">14.55</td>
    <td align="right">14.54</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">17.07</td>
    <td align="right">19.22</td>
    <td align="right">19.23</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.37</td>
    <td align="right">8.71</td>
    <td align="right">8.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">30.06</td>
    <td align="right">30.29</td>
    <td align="right">30.29</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">37.87</td>
    <td align="right">33.05</td>
    <td align="right">33.03</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.35</td>
    <td align="right">20.39</td>
    <td align="right">15.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">39.21</td>
    <td align="right">38.88</td>
    <td align="right">38.89</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">40.95</td>
    <td align="right">50.92</td>
    <td align="right">50.93</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">22.27</td>
    <td align="right">23.28</td>
    <td align="right">16.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4408</td>
    <td align="right">6.87</td>
    <td align="right">7.63</td>
    <td align="right">7.65</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">8.48</td>
    <td align="right">9.60</td>
    <td align="right">9.58</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.90</td>
    <td align="right">3.57</td>
    <td align="right">3.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">13.85</td>
    <td align="right">15.19</td>
    <td align="right">15.21</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">15.72</td>
    <td align="right">17.30</td>
    <td align="right">17.33</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">8.10</td>
    <td align="right">8.40</td>
    <td align="right">8.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">29.60</td>
    <td align="right">30.36</td>
    <td align="right">30.37</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">38.15</td>
    <td align="right">34.63</td>
    <td align="right">34.63</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">20.31</td>
    <td align="right">20.64</td>
    <td align="right">15.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">39.53</td>
    <td align="right">39.19</td>
    <td align="right">39.36</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">41.88</td>
    <td align="right">51.81</td>
    <td align="right">51.79</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">23.98</td>
    <td align="right">24.00</td>
    <td align="right">17.74</td>
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
    <td align="right">4.35</td>
    <td align="right">4.61</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.83</td>
    <td align="right">6.61</td>
    <td align="right">6.73</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">6.62</td>
    <td align="right">7.31</td>
    <td align="right">7.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">8.09</td>
    <td align="right">8.89</td>
    <td align="right">8.89</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.63</td>
    <td align="right">10.50</td>
    <td align="right">10.31</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.81</td>
    <td align="right">12.76</td>
    <td align="right">12.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.84</td>
    <td align="right">18.65</td>
    <td align="right">14.46</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.86</td>
    <td align="right">26.19</td>
    <td align="right">21.54</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">25.55</td>
    <td align="right">26.27</td>
    <td align="right">20.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">21.01</td>
    <td align="right">21.41</td>
    <td align="right">16.34</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">32.26</td>
    <td align="right">35.56</td>
    <td align="right">24.73</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.87</td>
    <td align="right">33.12</td>
    <td align="right">24.19</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4684</td>
    <td align="right">4.39</td>
    <td align="right">4.02</td>
    <td align="right">3.98</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">6.54</td>
    <td align="right">6.98</td>
    <td align="right">6.96</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">6.00</td>
    <td align="right">6.09</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">8.81</td>
    <td align="right">8.53</td>
    <td align="right">8.53</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">9.09</td>
    <td align="right">10.08</td>
    <td align="right">10.12</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">11.15</td>
    <td align="right">12.73</td>
    <td align="right">12.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">17.15</td>
    <td align="right">20.42</td>
    <td align="right">14.68</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">25.58</td>
    <td align="right">26.35</td>
    <td align="right">21.90</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">25.58</td>
    <td align="right">25.91</td>
    <td align="right">21.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">20.00</td>
    <td align="right">23.69</td>
    <td align="right">16.55</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">32.74</td>
    <td align="right">36.71</td>
    <td align="right">25.21</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">32.99</td>
    <td align="right">36.62</td>
    <td align="right">25.07</td>
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
    <td align="right">26.15</td>
    <td align="right">5.45</td>
    <td align="right">4.22</td>
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
    <td align="right">9.57</td>
    <td align="right">10.59</td>
    <td align="right">17.10</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.59</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.11</td>
    <td align="right">4.66</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.76</td>
    <td align="right">15.45</td>
    <td align="right">18.52</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.14</td>
    <td align="right">4.65</td>
    <td align="right">4.65</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.66</td>
    <td align="right">5.52</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.81</td>
    <td align="right">18.62</td>
    <td align="right">17.10</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.65</td>
    <td align="right">5.06</td>
    <td align="right">5.06</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.00</td>
    <td align="right">5.95</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.85</td>
    <td align="right">23.21</td>
    <td align="right">17.96</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.00</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.30</td>
    <td align="right">3.50</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1818</td>
    <td align="right">10.68</td>
    <td align="right">11.26</td>
    <td align="right">17.69</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">4.83</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.24</td>
    <td align="right">4.91</td>
    <td align="right">4.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">16.35</td>
    <td align="right">16.32</td>
    <td align="right">18.68</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">5.23</td>
    <td align="right">4.75</td>
    <td align="right">4.75</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">4.82</td>
    <td align="right">5.60</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">19.18</td>
    <td align="right">19.63</td>
    <td align="right">17.67</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.83</td>
    <td align="right">5.18</td>
    <td align="right">5.17</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.15</td>
    <td align="right">6.03</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">23.96</td>
    <td align="right">24.17</td>
    <td align="right">18.05</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">6.07</td>
    <td align="right">5.80</td>
    <td align="right">5.80</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">3.46</td>
    <td align="right">3.72</td>
    <td align="right">3.72</td>
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
    <td align="right">3.33</td>
    <td align="right">3.91</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.39</td>
    <td align="right">3.76</td>
    <td align="right">3.75</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.82</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.03</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.03</td>
    <td align="right">4.06</td>
    <td align="right">4.07</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.27</td>
    <td align="right">2.32</td>
    <td align="right">2.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.04</td>
    <td align="right">6.72</td>
    <td align="right">6.69</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.17</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.39</td>
    <td align="right">4.35</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.50</td>
    <td align="right">7.22</td>
    <td align="right">7.22</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.06</td>
    <td align="right">7.70</td>
    <td align="right">7.70</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.46</td>
    <td align="right">4.38</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">3.46</td>
    <td align="right">4.14</td>
    <td align="right">4.16</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">3.57</td>
    <td align="right">4.01</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">3.08</td>
    <td align="right">2.83</td>
    <td align="right">2.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">3.91</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">4.19</td>
    <td align="right">4.38</td>
    <td align="right">4.38</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">3.26</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">6.27</td>
    <td align="right">7.13</td>
    <td align="right">7.11</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">6.51</td>
    <td align="right">6.84</td>
    <td align="right">6.67</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.68</td>
    <td align="right">4.71</td>
    <td align="right">3.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">6.58</td>
    <td align="right">7.51</td>
    <td align="right">7.51</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">7.13</td>
    <td align="right">7.69</td>
    <td align="right">7.68</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">4.76</td>
    <td align="right">4.77</td>
    <td align="right">3.54</td>
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
    <td align="right">2.80</td>
    <td align="right">2.36</td>
    <td align="right">2.36</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.88</td>
    <td align="right">4.12</td>
    <td align="right">4.13</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.97</td>
    <td align="right">3.96</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.91</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.23</td>
    <td align="right">3.83</td>
    <td align="right">3.82</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.15</td>
    <td align="right">4.05</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.51</td>
    <td align="right">4.30</td>
    <td align="right">3.03</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.82</td>
    <td align="right">6.06</td>
    <td align="right">4.67</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">6.10</td>
    <td align="right">6.12</td>
    <td align="right">4.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.57</td>
    <td align="right">4.32</td>
    <td align="right">3.02</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.98</td>
    <td align="right">7.15</td>
    <td align="right">5.19</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.33</td>
    <td align="right">7.02</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4739</td>
    <td align="right">3.00</td>
    <td align="right">2.65</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">4.07</td>
    <td align="right">4.47</td>
    <td align="right">4.47</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">4.16</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.14</td>
    <td align="right">2.72</td>
    <td align="right">2.72</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">3.96</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">4.38</td>
    <td align="right">4.28</td>
    <td align="right">4.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.77</td>
    <td align="right">4.58</td>
    <td align="right">3.31</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">6.30</td>
    <td align="right">6.69</td>
    <td align="right">5.14</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">6.46</td>
    <td align="right">6.50</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">4.83</td>
    <td align="right">4.60</td>
    <td align="right">3.31</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.34</td>
    <td align="right">7.72</td>
    <td align="right">4.89</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">7.64</td>
    <td align="right">7.45</td>
    <td align="right">4.93</td>
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
    <td align="right">50.42</td>
    <td align="right">23.70</td>
    <td align="right">14.15</td>
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
    <td align="right">12.02</td>
    <td align="right">12.95</td>
    <td align="right">19.43</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.77</td>
    <td align="right">5.36</td>
    <td align="right">5.38</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.01</td>
    <td align="right">5.69</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">47.61</td>
    <td align="right">47.45</td>
    <td align="right">26.52</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.48</td>
    <td align="right">10.15</td>
    <td align="right">10.14</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.91</td>
    <td align="right">12.18</td>
    <td align="right">12.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">71.75</td>
    <td align="right">74.46</td>
    <td align="right">30.20</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.39</td>
    <td align="right">17.73</td>
    <td align="right">17.74</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.97</td>
    <td align="right">20.68</td>
    <td align="right">20.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">103.80</td>
    <td align="right">103.69</td>
    <td align="right">35.35</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.38</td>
    <td align="right">21.54</td>
    <td align="right">21.54</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.60</td>
    <td align="right">15.28</td>
    <td align="right">15.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1556</td>
    <td align="right">12.20</td>
    <td align="right">12.85</td>
    <td align="right">19.59</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">5.33</td>
    <td align="right">4.80</td>
    <td align="right">4.79</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">5.29</td>
    <td align="right">6.14</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">50.37</td>
    <td align="right">51.56</td>
    <td align="right">27.02</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">11.49</td>
    <td align="right">10.66</td>
    <td align="right">10.59</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">11.64</td>
    <td align="right">12.98</td>
    <td align="right">12.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">82.61</td>
    <td align="right">84.11</td>
    <td align="right">31.23</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">18.66</td>
    <td align="right">17.80</td>
    <td align="right">17.82</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">16.95</td>
    <td align="right">20.72</td>
    <td align="right">20.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.86</td>
    <td align="right">119.15</td>
    <td align="right">36.16</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">22.32</td>
    <td align="right">21.70</td>
    <td align="right">21.68</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">14.75</td>
    <td align="right">16.62</td>
    <td align="right">16.61</td>
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
    <td align="right">3.92</td>
    <td align="right">4.46</td>
    <td align="right">4.48</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.13</td>
    <td align="right">4.48</td>
    <td align="right">4.51</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.80</td>
    <td align="right">3.69</td>
    <td align="right">3.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.07</td>
    <td align="right">9.31</td>
    <td align="right">9.36</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.71</td>
    <td align="right">11.02</td>
    <td align="right">11.03</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.27</td>
    <td align="right">6.50</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.29</td>
    <td align="right">21.01</td>
    <td align="right">20.99</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.76</td>
    <td align="right">21.41</td>
    <td align="right">21.40</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.58</td>
    <td align="right">15.85</td>
    <td align="right">11.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.25</td>
    <td align="right">26.68</td>
    <td align="right">26.67</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.86</td>
    <td align="right">30.43</td>
    <td align="right">30.44</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">17.09</td>
    <td align="right">18.15</td>
    <td align="right">13.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4408</td>
    <td align="right">4.33</td>
    <td align="right">5.09</td>
    <td align="right">5.13</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">4.49</td>
    <td align="right">5.14</td>
    <td align="right">5.13</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">4.30</td>
    <td align="right">4.18</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">8.86</td>
    <td align="right">9.01</td>
    <td align="right">9.04</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">10.51</td>
    <td align="right">11.89</td>
    <td align="right">11.97</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">9.04</td>
    <td align="right">7.77</td>
    <td align="right">7.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">20.19</td>
    <td align="right">21.99</td>
    <td align="right">21.99</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">20.23</td>
    <td align="right">21.69</td>
    <td align="right">21.71</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">15.58</td>
    <td align="right">17.59</td>
    <td align="right">12.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">24.93</td>
    <td align="right">26.76</td>
    <td align="right">26.76</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">26.55</td>
    <td align="right">30.71</td>
    <td align="right">30.72</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">17.97</td>
    <td align="right">19.89</td>
    <td align="right">14.64</td>
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
    <td align="right">3.98</td>
    <td align="right">3.71</td>
    <td align="right">3.72</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.51</td>
    <td align="right">4.68</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.00</td>
    <td align="right">5.22</td>
    <td align="right">5.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.48</td>
    <td align="right">7.53</td>
    <td align="right">7.56</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.17</td>
    <td align="right">9.36</td>
    <td align="right">9.36</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">9.26</td>
    <td align="right">10.53</td>
    <td align="right">10.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.97</td>
    <td align="right">16.13</td>
    <td align="right">11.71</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.42</td>
    <td align="right">20.99</td>
    <td align="right">16.68</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">19.54</td>
    <td align="right">20.89</td>
    <td align="right">16.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.24</td>
    <td align="right">18.20</td>
    <td align="right">13.15</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">25.14</td>
    <td align="right">27.08</td>
    <td align="right">19.88</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">25.37</td>
    <td align="right">26.91</td>
    <td align="right">19.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4684</td>
    <td align="right">3.65</td>
    <td align="right">3.37</td>
    <td align="right">3.35</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">5.30</td>
    <td align="right">5.89</td>
    <td align="right">5.88</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">5.10</td>
    <td align="right">5.31</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">8.66</td>
    <td align="right">8.57</td>
    <td align="right">8.57</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">9.98</td>
    <td align="right">10.01</td>
    <td align="right">10.05</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">10.36</td>
    <td align="right">11.69</td>
    <td align="right">11.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">15.49</td>
    <td align="right">17.90</td>
    <td align="right">13.76</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">20.46</td>
    <td align="right">21.82</td>
    <td align="right">18.19</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">20.36</td>
    <td align="right">21.56</td>
    <td align="right">16.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">18.21</td>
    <td align="right">20.01</td>
    <td align="right">14.46</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">28.08</td>
    <td align="right">30.09</td>
    <td align="right">21.69</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">28.47</td>
    <td align="right">30.61</td>
    <td align="right">20.40</td>
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
    <td align="right">18.74</td>
    <td align="right">2.62</td>
    <td align="right">1.98</td>
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
    <td align="right">6.28</td>
    <td align="right">4.43</td>
    <td align="right">11.28</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.30</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.62</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.44</td>
    <td align="right">6.62</td>
    <td align="right">11.77</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.37</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.70</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.36</td>
    <td align="right">8.20</td>
    <td align="right">11.03</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.54</td>
    <td align="right">1.55</td>
    <td align="right">1.54</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.76</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.49</td>
    <td align="right">10.68</td>
    <td align="right">11.23</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.72</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.79</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1818</td>
    <td align="right">6.33</td>
    <td align="right">4.15</td>
    <td align="right">11.39</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">1.29</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">1.61</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">9.43</td>
    <td align="right">6.06</td>
    <td align="right">12.01</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">1.71</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">11.58</td>
    <td align="right">7.30</td>
    <td align="right">11.16</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">1.60</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">1.76</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">15.07</td>
    <td align="right">9.36</td>
    <td align="right">11.38</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">1.80</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
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
    <td align="right">2.24</td>
    <td align="right">1.69</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.30</td>
    <td align="right">1.75</td>
    <td align="right">1.77</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.03</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.17</td>
    <td align="right">1.93</td>
    <td align="right">1.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.80</td>
    <td align="right">2.19</td>
    <td align="right">2.28</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.50</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.10</td>
    <td align="right">2.93</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.01</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.99</td>
    <td align="right">2.42</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.69</td>
    <td align="right">3.68</td>
    <td align="right">3.68</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.79</td>
    <td align="right">4.30</td>
    <td align="right">4.30</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">2.91</td>
    <td align="right">2.90</td>
    <td align="right">1.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.23</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.32</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.01</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.19</td>
    <td align="right">1.93</td>
    <td align="right">1.93</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">2.77</td>
    <td align="right">2.20</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">1.52</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">4.08</td>
    <td align="right">2.89</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.15</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">2.98</td>
    <td align="right">2.43</td>
    <td align="right">1.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">4.66</td>
    <td align="right">3.72</td>
    <td align="right">3.71</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">4.73</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">2.93</td>
    <td align="right">2.94</td>
    <td align="right">1.75</td>
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
    <td align="right">2.03</td>
    <td align="right">1.71</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.23</td>
    <td align="right">1.74</td>
    <td align="right">1.72</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.28</td>
    <td align="right">1.75</td>
    <td align="right">1.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.08</td>
    <td align="right">1.61</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.18</td>
    <td align="right">1.93</td>
    <td align="right">1.92</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.71</td>
    <td align="right">2.26</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.90</td>
    <td align="right">2.38</td>
    <td align="right">1.74</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.13</td>
    <td align="right">2.90</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.02</td>
    <td align="right">2.91</td>
    <td align="right">2.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.89</td>
    <td align="right">2.88</td>
    <td align="right">1.73</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.63</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.68</td>
    <td align="right">4.33</td>
    <td align="right">4.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4739</td>
    <td align="right">2.01</td>
    <td align="right">1.69</td>
    <td align="right">1.67</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.24</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">2.28</td>
    <td align="right">1.74</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">2.05</td>
    <td align="right">1.60</td>
    <td align="right">1.59</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">2.19</td>
    <td align="right">1.92</td>
    <td align="right">1.92</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">2.76</td>
    <td align="right">2.20</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">2.98</td>
    <td align="right">2.39</td>
    <td align="right">1.74</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">4.05</td>
    <td align="right">2.87</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">4.07</td>
    <td align="right">2.96</td>
    <td align="right">2.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">2.95</td>
    <td align="right">2.88</td>
    <td align="right">1.77</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">4.69</td>
    <td align="right">3.76</td>
    <td align="right">3.78</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">4.82</td>
    <td align="right">4.31</td>
    <td align="right">4.37</td>
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
    <td align="right">24.06</td>
    <td align="right">11.11</td>
    <td align="right">5.68</td>
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
    <td align="right">7.77</td>
    <td align="right">6.23</td>
    <td align="right">12.86</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">1.98</td>
    <td align="right">1.92</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.12</td>
    <td align="right">2.03</td>
    <td align="right">2.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">12.93</td>
    <td align="right">11.27</td>
    <td align="right">15.67</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">2.95</td>
    <td align="right">3.16</td>
    <td align="right">3.22</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.28</td>
    <td align="right">3.17</td>
    <td align="right">3.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.46</td>
    <td align="right">24.83</td>
    <td align="right">18.24</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.78</td>
    <td align="right">5.79</td>
    <td align="right">6.07</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.90</td>
    <td align="right">6.32</td>
    <td align="right">6.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">55.10</td>
    <td align="right">41.23</td>
    <td align="right">20.62</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.67</td>
    <td align="right">7.56</td>
    <td align="right">7.59</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.91</td>
    <td align="right">6.45</td>
    <td align="right">6.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1556</td>
    <td align="right">7.66</td>
    <td align="right">6.12</td>
    <td align="right">12.96</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">2.04</td>
    <td align="right">1.99</td>
    <td align="right">1.99</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">2.12</td>
    <td align="right">2.03</td>
    <td align="right">2.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">12.93</td>
    <td align="right">10.95</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">3.67</td>
    <td align="right">3.55</td>
    <td align="right">3.60</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">3.47</td>
    <td align="right">3.33</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">30.39</td>
    <td align="right">23.23</td>
    <td align="right">17.80</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">6.38</td>
    <td align="right">6.01</td>
    <td align="right">5.93</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">6.85</td>
    <td align="right">6.17</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.71</td>
    <td align="right">38.01</td>
    <td align="right">21.04</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">8.95</td>
    <td align="right">7.66</td>
    <td align="right">8.14</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">7.64</td>
    <td align="right">6.44</td>
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
    <td align="right">2.4515</td>
    <td align="right">2.72</td>
    <td align="right">2.52</td>
    <td align="right">2.51</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.74</td>
    <td align="right">2.61</td>
    <td align="right">2.63</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.42</td>
    <td align="right">2.56</td>
    <td align="right">2.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.04</td>
    <td align="right">4.54</td>
    <td align="right">4.49</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.10</td>
    <td align="right">4.77</td>
    <td align="right">5.08</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.97</td>
    <td align="right">3.50</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.15</td>
    <td align="right">9.35</td>
    <td align="right">9.65</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.72</td>
    <td align="right">9.44</td>
    <td align="right">9.40</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.76</td>
    <td align="right">8.00</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.27</td>
    <td align="right">13.12</td>
    <td align="right">13.13</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.12</td>
    <td align="right">16.82</td>
    <td align="right">16.67</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.09</td>
    <td align="right">10.86</td>
    <td align="right">6.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4408</td>
    <td align="right">2.70</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.75</td>
    <td align="right">2.61</td>
    <td align="right">2.61</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">2.42</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.95</td>
    <td align="right">4.54</td>
    <td align="right">4.42</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.36</td>
    <td align="right">4.85</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">3.00</td>
    <td align="right">3.30</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">10.04</td>
    <td align="right">9.09</td>
    <td align="right">9.06</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">10.94</td>
    <td align="right">9.58</td>
    <td align="right">9.15</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">8.16</td>
    <td align="right">8.40</td>
    <td align="right">5.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">15.88</td>
    <td align="right">14.48</td>
    <td align="right">14.30</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">15.94</td>
    <td align="right">16.08</td>
    <td align="right">16.72</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">9.73</td>
    <td align="right">11.61</td>
    <td align="right">6.88</td>
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
    <td align="right">2.55</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.72</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.75</td>
    <td align="right">2.61</td>
    <td align="right">2.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.05</td>
    <td align="right">3.01</td>
    <td align="right">3.06</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.96</td>
    <td align="right">4.32</td>
    <td align="right">4.38</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.21</td>
    <td align="right">4.91</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.03</td>
    <td align="right">8.33</td>
    <td align="right">5.61</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.04</td>
    <td align="right">9.59</td>
    <td align="right">9.76</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.16</td>
    <td align="right">9.41</td>
    <td align="right">9.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.63</td>
    <td align="right">11.14</td>
    <td align="right">6.51</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.88</td>
    <td align="right">14.16</td>
    <td align="right">14.83</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.43</td>
    <td align="right">16.99</td>
    <td align="right">16.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4684</td>
    <td align="right">2.36</td>
    <td align="right">2.49</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4408</td>
    <td align="right">2.69</td>
    <td align="right">2.51</td>
    <td align="right">2.51</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">2.69</td>
    <td align="right">2.57</td>
    <td align="right">2.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">2.74</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">3.57</td>
    <td align="right">3.94</td>
    <td align="right">3.98</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">4.02</td>
    <td align="right">4.65</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">7.34</td>
    <td align="right">7.44</td>
    <td align="right">5.11</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">9.55</td>
    <td align="right">8.73</td>
    <td align="right">8.74</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">9.49</td>
    <td align="right">8.55</td>
    <td align="right">8.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">9.28</td>
    <td align="right">10.17</td>
    <td align="right">6.03</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">13.99</td>
    <td align="right">13.01</td>
    <td align="right">13.01</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">14.68</td>
    <td align="right">15.23</td>
    <td align="right">15.15</td>
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
    <td align="right">25.08</td>
    <td align="right">5.25</td>
    <td align="right">3.80</td>
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
    <td align="right">9.24</td>
    <td align="right">10.51</td>
    <td align="right">13.91</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.72</td>
    <td align="right">3.44</td>
    <td align="right">3.46</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.27</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.55</td>
    <td align="right">14.72</td>
    <td align="right">14.26</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.30</td>
    <td align="right">3.86</td>
    <td align="right">3.85</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.96</td>
    <td align="right">4.74</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.17</td>
    <td align="right">18.15</td>
    <td align="right">13.65</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.13</td>
    <td align="right">4.28</td>
    <td align="right">4.22</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.56</td>
    <td align="right">5.11</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.45</td>
    <td align="right">54.79</td>
    <td align="right">18.19</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.52</td>
    <td align="right">4.62</td>
    <td align="right">4.63</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.17</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1818</td>
    <td align="right">10.28</td>
    <td align="right">11.32</td>
    <td align="right">14.32</td>
    <td align="center">4</td>
    <td align="right">3.3670</td>
    <td align="right">3.82</td>
    <td align="right">3.58</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">3.0480</td>
    <td align="right">4.36</td>
    <td align="right">4.13</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3131</td>
    <td align="right">15.12</td>
    <td align="right">15.95</td>
    <td align="right">14.77</td>
    <td align="center">5</td>
    <td align="right">1.0454</td>
    <td align="right">4.41</td>
    <td align="right">4.01</td>
    <td align="right">3.99</td>
    <td align="center">6</td>
    <td align="right">0.8156</td>
    <td align="right">5.04</td>
    <td align="right">4.77</td>
    <td align="right">4.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0462</td>
    <td align="right">18.26</td>
    <td align="right">20.35</td>
    <td align="right">13.93</td>
    <td align="center">6</td>
    <td align="right">0.4073</td>
    <td align="right">5.42</td>
    <td align="right">4.38</td>
    <td align="right">4.38</td>
    <td align="center">7</td>
    <td align="right">0.2848</td>
    <td align="right">5.66</td>
    <td align="right">5.07</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">22.84</td>
    <td align="right">51.78</td>
    <td align="right">17.45</td>
    <td align="center">7</td>
    <td align="right">0.1956</td>
    <td align="right">7.14</td>
    <td align="right">4.68</td>
    <td align="right">4.68</td>
    <td align="center">8</td>
    <td align="right">0.1228</td>
    <td align="right">6.29</td>
    <td align="right">5.58</td>
    <td align="right">5.52</td>
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
    <td align="right">5.28</td>
    <td align="right">4.30</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">7.84</td>
    <td align="right">4.58</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.85</td>
    <td align="right">2.10</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.16</td>
    <td align="right">7.07</td>
    <td align="right">7.02</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">14.05</td>
    <td align="right">6.86</td>
    <td align="right">6.82</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.79</td>
    <td align="right">2.92</td>
    <td align="right">2.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.47</td>
    <td align="right">10.03</td>
    <td align="right">9.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">12.55</td>
    <td align="right">10.63</td>
    <td align="right">10.63</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.28</td>
    <td align="right">4.36</td>
    <td align="right">3.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.61</td>
    <td align="right">11.11</td>
    <td align="right">11.08</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.92</td>
    <td align="right">12.35</td>
    <td align="right">12.23</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.43</td>
    <td align="right">4.39</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">5.39</td>
    <td align="right">4.40</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">2.3163</td>
    <td align="right">7.46</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">2.7392</td>
    <td align="right">2.85</td>
    <td align="right">2.19</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4226</td>
    <td align="right">8.28</td>
    <td align="right">6.97</td>
    <td align="right">6.98</td>
    <td align="center">8</td>
    <td align="right">0.3730</td>
    <td align="right">12.71</td>
    <td align="right">6.96</td>
    <td align="right">6.95</td>
    <td align="center">8</td>
    <td align="right">0.5386</td>
    <td align="right">2.74</td>
    <td align="right">2.95</td>
    <td align="right">2.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0752</td>
    <td align="right">10.54</td>
    <td align="right">10.13</td>
    <td align="right">10.10</td>
    <td align="center">11</td>
    <td align="right">0.0634</td>
    <td align="right">12.12</td>
    <td align="right">10.65</td>
    <td align="right">10.53</td>
    <td align="center">11</td>
    <td align="right">0.1201</td>
    <td align="right">4.33</td>
    <td align="right">4.45</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0135</td>
    <td align="right">11.58</td>
    <td align="right">11.05</td>
    <td align="right">11.01</td>
    <td align="center">14</td>
    <td align="right">0.0146</td>
    <td align="right">14.17</td>
    <td align="right">12.41</td>
    <td align="right">12.36</td>
    <td align="center">13</td>
    <td align="right">0.0319</td>
    <td align="right">6.77</td>
    <td align="right">4.45</td>
    <td align="right">3.09</td>
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
    <td align="right">2.80</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.71</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.77</td>
    <td align="right">2.99</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.24</td>
    <td align="right">3.26</td>
    <td align="right">2.62</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.18</td>
    <td align="right">3.78</td>
    <td align="right">3.20</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">5.98</td>
    <td align="right">4.49</td>
    <td align="right">3.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.52</td>
    <td align="right">4.22</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.80</td>
    <td align="right">6.29</td>
    <td align="right">4.81</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.23</td>
    <td align="right">6.22</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.41</td>
    <td align="right">4.21</td>
    <td align="right">2.87</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.94</td>
    <td align="right">17.57</td>
    <td align="right">13.32</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.74</td>
    <td align="right">6.67</td>
    <td align="right">4.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4739</td>
    <td align="right">2.81</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">2.4715</td>
    <td align="right">3.73</td>
    <td align="right">3.27</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.3106</td>
    <td align="right">3.77</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4474</td>
    <td align="right">3.23</td>
    <td align="right">3.37</td>
    <td align="right">2.72</td>
    <td align="center">8</td>
    <td align="right">0.4256</td>
    <td align="right">4.17</td>
    <td align="right">3.91</td>
    <td align="right">3.29</td>
    <td align="center">8</td>
    <td align="right">0.3856</td>
    <td align="right">5.68</td>
    <td align="right">4.60</td>
    <td align="right">3.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0914</td>
    <td align="right">4.36</td>
    <td align="right">4.25</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">0.0757</td>
    <td align="right">9.67</td>
    <td align="right">6.42</td>
    <td align="right">5.06</td>
    <td align="center">11</td>
    <td align="right">0.0638</td>
    <td align="right">7.70</td>
    <td align="right">6.29</td>
    <td align="right">4.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0191</td>
    <td align="right">5.34</td>
    <td align="right">4.30</td>
    <td align="right">2.97</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">7.81</td>
    <td align="right">7.07</td>
    <td align="right">5.07</td>
    <td align="center">14</td>
    <td align="right">0.0125</td>
    <td align="right">9.38</td>
    <td align="right">15.56</td>
    <td align="right">12.05</td>
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
    <td align="right">23.28</td>
    <td align="right">11.91</td>
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
    <td align="right">15.10</td>
    <td align="right">11.06</td>
    <td align="right">15.24</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.01</td>
    <td align="right">3.65</td>
    <td align="right">3.73</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.60</td>
    <td align="right">4.41</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">57.07</td>
    <td align="right">66.75</td>
    <td align="right">28.23</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.00</td>
    <td align="right">5.70</td>
    <td align="right">5.63</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.80</td>
    <td align="right">6.58</td>
    <td align="right">6.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">69.57</td>
    <td align="right">73.68</td>
    <td align="right">24.65</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.19</td>
    <td align="right">16.88</td>
    <td align="right">16.88</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.16</td>
    <td align="right">15.73</td>
    <td align="right">15.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">96.81</td>
    <td align="right">111.21</td>
    <td align="right">30.12</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.53</td>
    <td align="right">16.68</td>
    <td align="right">16.41</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.49</td>
    <td align="right">22.59</td>
    <td align="right">22.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1556</td>
    <td align="right">17.04</td>
    <td align="right">45.59</td>
    <td align="right">27.12</td>
    <td align="center">4</td>
    <td align="right">3.3474</td>
    <td align="right">4.20</td>
    <td align="right">13.27</td>
    <td align="right">13.22</td>
    <td align="center">5</td>
    <td align="right">3.0451</td>
    <td align="right">4.69</td>
    <td align="right">4.52</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3152</td>
    <td align="right">50.99</td>
    <td align="right">70.65</td>
    <td align="right">29.48</td>
    <td align="center">5</td>
    <td align="right">1.0335</td>
    <td align="right">7.94</td>
    <td align="right">6.27</td>
    <td align="right">6.32</td>
    <td align="center">6</td>
    <td align="right">0.8296</td>
    <td align="right">7.02</td>
    <td align="right">6.54</td>
    <td align="right">6.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0452</td>
    <td align="right">74.90</td>
    <td align="right">78.78</td>
    <td align="right">25.84</td>
    <td align="center">6</td>
    <td align="right">0.4069</td>
    <td align="right">15.37</td>
    <td align="right">13.50</td>
    <td align="right">13.54</td>
    <td align="center">7</td>
    <td align="right">0.2911</td>
    <td align="right">16.27</td>
    <td align="right">15.56</td>
    <td align="right">15.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.21</td>
    <td align="right">119.32</td>
    <td align="right">31.74</td>
    <td align="center">7</td>
    <td align="right">0.1900</td>
    <td align="right">19.71</td>
    <td align="right">18.31</td>
    <td align="right">18.24</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">20.88</td>
    <td align="right">23.31</td>
    <td align="right">23.16</td>
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
    <td align="right">6.06</td>
    <td align="right">4.69</td>
    <td align="right">4.65</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.03</td>
    <td align="right">4.92</td>
    <td align="right">5.06</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.12</td>
    <td align="right">2.23</td>
    <td align="right">2.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.81</td>
    <td align="right">19.48</td>
    <td align="right">19.53</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.51</td>
    <td align="right">20.10</td>
    <td align="right">20.04</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.72</td>
    <td align="right">4.65</td>
    <td align="right">4.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">27.21</td>
    <td align="right">25.62</td>
    <td align="right">25.67</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">31.08</td>
    <td align="right">28.25</td>
    <td align="right">28.21</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.05</td>
    <td align="right">15.37</td>
    <td align="right">10.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">35.90</td>
    <td align="right">35.53</td>
    <td align="right">35.44</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">39.53</td>
    <td align="right">37.13</td>
    <td align="right">37.16</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.32</td>
    <td align="right">17.86</td>
    <td align="right">12.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4408</td>
    <td align="right">6.17</td>
    <td align="right">4.75</td>
    <td align="right">4.72</td>
    <td align="center">5</td>
    <td align="right">2.3114</td>
    <td align="right">7.67</td>
    <td align="right">17.69</td>
    <td align="right">17.61</td>
    <td align="center">5</td>
    <td align="right">2.7422</td>
    <td align="right">3.18</td>
    <td align="right">2.33</td>
    <td align="right">2.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4214</td>
    <td align="right">10.47</td>
    <td align="right">17.58</td>
    <td align="right">17.36</td>
    <td align="center">8</td>
    <td align="right">0.3763</td>
    <td align="right">19.21</td>
    <td align="right">9.06</td>
    <td align="right">8.99</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">4.78</td>
    <td align="right">11.55</td>
    <td align="right">9.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0760</td>
    <td align="right">27.44</td>
    <td align="right">25.83</td>
    <td align="right">25.84</td>
    <td align="center">11</td>
    <td align="right">0.0633</td>
    <td align="right">34.53</td>
    <td align="right">30.26</td>
    <td align="right">30.24</td>
    <td align="center">11</td>
    <td align="right">0.1206</td>
    <td align="right">14.03</td>
    <td align="right">15.37</td>
    <td align="right">10.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0156</td>
    <td align="right">36.04</td>
    <td align="right">35.58</td>
    <td align="right">35.65</td>
    <td align="center">14</td>
    <td align="right">0.0111</td>
    <td align="right">39.47</td>
    <td align="right">38.18</td>
    <td align="right">38.13</td>
    <td align="center">13</td>
    <td align="right">0.0282</td>
    <td align="right">16.47</td>
    <td align="right">17.93</td>
    <td align="right">12.36</td>
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
    <td align="right">3.07</td>
    <td align="right">2.02</td>
    <td align="right">2.14</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.04</td>
    <td align="right">3.40</td>
    <td align="right">3.44</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.11</td>
    <td align="right">3.16</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.08</td>
    <td align="right">5.48</td>
    <td align="right">4.64</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">6.03</td>
    <td align="right">5.85</td>
    <td align="right">5.28</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.99</td>
    <td align="right">6.45</td>
    <td align="right">5.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.28</td>
    <td align="right">15.23</td>
    <td align="right">10.74</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.86</td>
    <td align="right">24.17</td>
    <td align="right">19.93</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">23.32</td>
    <td align="right">18.94</td>
    <td align="right">15.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.74</td>
    <td align="right">17.80</td>
    <td align="right">12.26</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.21</td>
    <td align="right">26.55</td>
    <td align="right">18.77</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.47</td>
    <td align="right">24.30</td>
    <td align="right">18.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4684</td>
    <td align="right">3.08</td>
    <td align="right">2.17</td>
    <td align="right">2.21</td>
    <td align="center">5</td>
    <td align="right">2.4638</td>
    <td align="right">4.05</td>
    <td align="right">3.42</td>
    <td align="right">3.48</td>
    <td align="center">5</td>
    <td align="right">2.3236</td>
    <td align="right">4.13</td>
    <td align="right">3.32</td>
    <td align="right">3.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4407</td>
    <td align="right">5.28</td>
    <td align="right">5.33</td>
    <td align="right">4.59</td>
    <td align="center">8</td>
    <td align="right">0.4233</td>
    <td align="right">6.97</td>
    <td align="right">6.55</td>
    <td align="right">6.05</td>
    <td align="center">8</td>
    <td align="right">0.3785</td>
    <td align="right">9.29</td>
    <td align="right">14.78</td>
    <td align="right">13.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0864</td>
    <td align="right">14.28</td>
    <td align="right">15.32</td>
    <td align="right">10.89</td>
    <td align="center">11</td>
    <td align="right">0.0777</td>
    <td align="right">23.08</td>
    <td align="right">22.80</td>
    <td align="right">18.98</td>
    <td align="center">11</td>
    <td align="right">0.0640</td>
    <td align="right">20.80</td>
    <td align="right">23.40</td>
    <td align="right">19.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">17.80</td>
    <td align="right">17.98</td>
    <td align="right">12.31</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">29.13</td>
    <td align="right">27.35</td>
    <td align="right">19.30</td>
    <td align="center">14</td>
    <td align="right">0.0114</td>
    <td align="right">28.49</td>
    <td align="right">26.83</td>
    <td align="right">18.95</td>
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
    <td align="right">74.14</td>
    <td align="right">35.09</td>
    <td align="right">14.26</td>
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
    <td align="right">27.58</td>
    <td align="right">44.01</td>
    <td align="right">37.73</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">13.36</td>
    <td align="right">18.29</td>
    <td align="right">18.28</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.18</td>
    <td align="right">20.07</td>
    <td align="right">20.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">41.81</td>
    <td align="right">67.97</td>
    <td align="right">40.24</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">18.31</td>
    <td align="right">21.44</td>
    <td align="right">21.37</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.00</td>
    <td align="right">18.84</td>
    <td align="right">18.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">51.58</td>
    <td align="right">84.21</td>
    <td align="right">39.12</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.46</td>
    <td align="right">19.30</td>
    <td align="right">19.11</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.21</td>
    <td align="right">21.12</td>
    <td align="right">21.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">64.51</td>
    <td align="right">103.49</td>
    <td align="right">40.61</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.56</td>
    <td align="right">20.59</td>
    <td align="right">20.59</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.13</td>
    <td align="right">23.11</td>
    <td align="right">22.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1768</td>
    <td align="right">31.64</td>
    <td align="right">44.28</td>
    <td align="right">37.80</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">13.60</td>
    <td align="right">16.38</td>
    <td align="right">16.46</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">14.75</td>
    <td align="right">18.28</td>
    <td align="right">18.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">46.65</td>
    <td align="right">66.83</td>
    <td align="right">40.67</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">15.47</td>
    <td align="right">18.93</td>
    <td align="right">18.81</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">16.14</td>
    <td align="right">18.51</td>
    <td align="right">18.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">57.23</td>
    <td align="right">83.01</td>
    <td align="right">40.12</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">16.71</td>
    <td align="right">18.89</td>
    <td align="right">18.92</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">17.26</td>
    <td align="right">20.92</td>
    <td align="right">21.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">73.40</td>
    <td align="right">111.58</td>
    <td align="right">41.79</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">17.82</td>
    <td align="right">21.65</td>
    <td align="right">21.65</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">19.51</td>
    <td align="right">23.03</td>
    <td align="right">21.90</td>
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
    <td align="right">19.58</td>
    <td align="right">22.09</td>
    <td align="right">22.39</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.64</td>
    <td align="right">25.62</td>
    <td align="right">25.61</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">12.09</td>
    <td align="right">15.52</td>
    <td align="right">15.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.86</td>
    <td align="right">29.62</td>
    <td align="right">29.64</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.21</td>
    <td align="right">32.43</td>
    <td align="right">32.53</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">14.16</td>
    <td align="right">17.82</td>
    <td align="right">17.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.85</td>
    <td align="right">35.36</td>
    <td align="right">35.35</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.39</td>
    <td align="right">48.08</td>
    <td align="right">48.16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">16.36</td>
    <td align="right">20.82</td>
    <td align="right">20.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.00</td>
    <td align="right">39.86</td>
    <td align="right">39.74</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.87</td>
    <td align="right">56.27</td>
    <td align="right">56.61</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.69</td>
    <td align="right">25.02</td>
    <td align="right">25.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4301</td>
    <td align="right">19.96</td>
    <td align="right">23.17</td>
    <td align="right">23.23</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">26.31</td>
    <td align="right">26.71</td>
    <td align="right">26.76</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">12.65</td>
    <td align="right">16.20</td>
    <td align="right">15.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">26.85</td>
    <td align="right">29.98</td>
    <td align="right">29.77</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">37.56</td>
    <td align="right">34.48</td>
    <td align="right">34.49</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">15.10</td>
    <td align="right">18.17</td>
    <td align="right">18.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">33.53</td>
    <td align="right">36.83</td>
    <td align="right">36.83</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">69.62</td>
    <td align="right">48.36</td>
    <td align="right">48.44</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">17.02</td>
    <td align="right">21.11</td>
    <td align="right">21.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">37.86</td>
    <td align="right">42.01</td>
    <td align="right">42.00</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">82.77</td>
    <td align="right">57.30</td>
    <td align="right">57.20</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">25.06</td>
    <td align="right">26.24</td>
    <td align="right">26.17</td>
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
    <td align="right">14.10</td>
    <td align="right">15.74</td>
    <td align="right">16.03</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.49</td>
    <td align="right">22.09</td>
    <td align="right">22.06</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.65</td>
    <td align="right">25.64</td>
    <td align="right">25.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">18.87</td>
    <td align="right">19.03</td>
    <td align="right">19.05</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.01</td>
    <td align="right">29.60</td>
    <td align="right">29.63</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.21</td>
    <td align="right">32.42</td>
    <td align="right">32.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">23.66</td>
    <td align="right">23.95</td>
    <td align="right">23.58</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.76</td>
    <td align="right">35.37</td>
    <td align="right">35.37</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.40</td>
    <td align="right">48.07</td>
    <td align="right">48.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">30.85</td>
    <td align="right">32.00</td>
    <td align="right">32.00</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">35.95</td>
    <td align="right">39.78</td>
    <td align="right">39.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.88</td>
    <td align="right">56.23</td>
    <td align="right">56.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4960</td>
    <td align="right">14.27</td>
    <td align="right">17.37</td>
    <td align="right">17.36</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">20.09</td>
    <td align="right">23.22</td>
    <td align="right">23.24</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">26.34</td>
    <td align="right">26.75</td>
    <td align="right">26.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">19.44</td>
    <td align="right">20.16</td>
    <td align="right">20.16</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">26.87</td>
    <td align="right">29.98</td>
    <td align="right">29.82</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">38.72</td>
    <td align="right">34.48</td>
    <td align="right">34.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">22.68</td>
    <td align="right">24.72</td>
    <td align="right">24.58</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">33.45</td>
    <td align="right">36.95</td>
    <td align="right">36.95</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">69.65</td>
    <td align="right">48.37</td>
    <td align="right">48.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">31.04</td>
    <td align="right">34.55</td>
    <td align="right">34.56</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">37.71</td>
    <td align="right">42.03</td>
    <td align="right">42.03</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">82.82</td>
    <td align="right">57.37</td>
    <td align="right">57.28</td>
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
    <td align="right">107.65</td>
    <td align="right">125.85</td>
    <td align="right">27.13</td>
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
    <td align="right">34.08</td>
    <td align="right">54.17</td>
    <td align="right">45.96</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.62</td>
    <td align="right">21.05</td>
    <td align="right">20.98</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">20.27</td>
    <td align="right">24.94</td>
    <td align="right">24.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">101.89</td>
    <td align="right">146.11</td>
    <td align="right">63.77</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">28.59</td>
    <td align="right">35.48</td>
    <td align="right">35.41</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">23.88</td>
    <td align="right">28.68</td>
    <td align="right">28.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">177.18</td>
    <td align="right">254.77</td>
    <td align="right">79.52</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.57</td>
    <td align="right">45.59</td>
    <td align="right">45.23</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">38.27</td>
    <td align="right">49.35</td>
    <td align="right">49.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">267.53</td>
    <td align="right">404.74</td>
    <td align="right">98.53</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.29</td>
    <td align="right">62.32</td>
    <td align="right">62.30</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">60.38</td>
    <td align="right">63.69</td>
    <td align="right">63.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1542</td>
    <td align="right">38.13</td>
    <td align="right">53.75</td>
    <td align="right">44.92</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">14.86</td>
    <td align="right">17.56</td>
    <td align="right">17.53</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.43</td>
    <td align="right">20.65</td>
    <td align="right">19.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">98.31</td>
    <td align="right">128.80</td>
    <td align="right">59.89</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">24.44</td>
    <td align="right">28.33</td>
    <td align="right">27.90</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">27.41</td>
    <td align="right">32.32</td>
    <td align="right">31.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">190.95</td>
    <td align="right">246.90</td>
    <td align="right">77.80</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">38.19</td>
    <td align="right">46.04</td>
    <td align="right">45.86</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">39.47</td>
    <td align="right">49.06</td>
    <td align="right">49.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">299.04</td>
    <td align="right">408.82</td>
    <td align="right">99.43</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">46.98</td>
    <td align="right">63.47</td>
    <td align="right">63.13</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">62.59</td>
    <td align="right">64.91</td>
    <td align="right">65.01</td>
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
    <td align="right">25.19</td>
    <td align="right">27.80</td>
    <td align="right">27.84</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.22</td>
    <td align="right">33.98</td>
    <td align="right">32.96</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">14.28</td>
    <td align="right">19.30</td>
    <td align="right">19.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">39.09</td>
    <td align="right">42.78</td>
    <td align="right">42.79</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">50.32</td>
    <td align="right">46.75</td>
    <td align="right">46.77</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">23.05</td>
    <td align="right">27.15</td>
    <td align="right">27.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">64.53</td>
    <td align="right">70.41</td>
    <td align="right">69.15</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">102.83</td>
    <td align="right">81.27</td>
    <td align="right">81.32</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">41.31</td>
    <td align="right">44.50</td>
    <td align="right">44.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.15</td>
    <td align="right">92.31</td>
    <td align="right">92.38</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">133.32</td>
    <td align="right">107.13</td>
    <td align="right">107.32</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">69.08</td>
    <td align="right">72.87</td>
    <td align="right">72.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4524</td>
    <td align="right">22.30</td>
    <td align="right">25.84</td>
    <td align="right">25.80</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">30.37</td>
    <td align="right">33.39</td>
    <td align="right">33.38</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">14.95</td>
    <td align="right">18.26</td>
    <td align="right">18.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">39.85</td>
    <td align="right">44.26</td>
    <td align="right">43.99</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">53.47</td>
    <td align="right">51.73</td>
    <td align="right">51.69</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">25.54</td>
    <td align="right">26.86</td>
    <td align="right">26.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">67.21</td>
    <td align="right">72.80</td>
    <td align="right">72.78</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">104.21</td>
    <td align="right">82.19</td>
    <td align="right">82.12</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">43.13</td>
    <td align="right">45.42</td>
    <td align="right">45.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">88.23</td>
    <td align="right">92.39</td>
    <td align="right">92.55</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.54</td>
    <td align="right">107.79</td>
    <td align="right">107.83</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">70.78</td>
    <td align="right">77.18</td>
    <td align="right">77.20</td>
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
    <td align="right">16.90</td>
    <td align="right">19.50</td>
    <td align="right">19.32</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">24.80</td>
    <td align="right">27.60</td>
    <td align="right">27.60</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.64</td>
    <td align="right">31.18</td>
    <td align="right">31.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">30.13</td>
    <td align="right">29.61</td>
    <td align="right">29.50</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">40.08</td>
    <td align="right">44.30</td>
    <td align="right">44.19</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">55.49</td>
    <td align="right">53.20</td>
    <td align="right">53.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">47.91</td>
    <td align="right">48.26</td>
    <td align="right">48.20</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">69.00</td>
    <td align="right">72.60</td>
    <td align="right">72.59</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">104.37</td>
    <td align="right">82.75</td>
    <td align="right">82.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">80.66</td>
    <td align="right">84.40</td>
    <td align="right">84.42</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.42</td>
    <td align="right">92.55</td>
    <td align="right">92.64</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.74</td>
    <td align="right">107.32</td>
    <td align="right">107.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4684</td>
    <td align="right">15.53</td>
    <td align="right">19.13</td>
    <td align="right">19.23</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">24.33</td>
    <td align="right">27.56</td>
    <td align="right">27.61</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">30.43</td>
    <td align="right">33.47</td>
    <td align="right">33.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">30.82</td>
    <td align="right">30.08</td>
    <td align="right">30.64</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">39.17</td>
    <td align="right">43.90</td>
    <td align="right">43.69</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">56.96</td>
    <td align="right">54.06</td>
    <td align="right">54.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">46.93</td>
    <td align="right">53.83</td>
    <td align="right">53.80</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">69.03</td>
    <td align="right">74.23</td>
    <td align="right">74.22</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">102.63</td>
    <td align="right">80.76</td>
    <td align="right">80.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">81.53</td>
    <td align="right">87.08</td>
    <td align="right">87.27</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">88.41</td>
    <td align="right">93.27</td>
    <td align="right">93.30</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.62</td>
    <td align="right">109.61</td>
    <td align="right">109.61</td>
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
    <td align="right">79.09</td>
    <td align="right">14.12</td>
    <td align="right">8.56</td>
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
    <td align="right">15.93</td>
    <td align="right">23.06</td>
    <td align="right">26.72</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.09</td>
    <td align="right">13.45</td>
    <td align="right">13.45</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.85</td>
    <td align="right">16.20</td>
    <td align="right">16.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">22.30</td>
    <td align="right">34.01</td>
    <td align="right">29.06</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">15.36</td>
    <td align="right">16.61</td>
    <td align="right">16.62</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.13</td>
    <td align="right">18.77</td>
    <td align="right">18.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">27.95</td>
    <td align="right">46.48</td>
    <td align="right">29.12</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.62</td>
    <td align="right">19.17</td>
    <td align="right">19.20</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">20.70</td>
    <td align="right">21.59</td>
    <td align="right">22.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">35.68</td>
    <td align="right">58.37</td>
    <td align="right">30.05</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">21.06</td>
    <td align="right">22.03</td>
    <td align="right">22.04</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">23.28</td>
    <td align="right">24.21</td>
    <td align="right">24.21</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1768</td>
    <td align="right">20.57</td>
    <td align="right">27.97</td>
    <td align="right">27.88</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">12.19</td>
    <td align="right">13.54</td>
    <td align="right">13.56</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">15.44</td>
    <td align="right">17.07</td>
    <td align="right">17.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">30.84</td>
    <td align="right">42.23</td>
    <td align="right">30.29</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">15.85</td>
    <td align="right">17.45</td>
    <td align="right">17.44</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">17.77</td>
    <td align="right">20.06</td>
    <td align="right">19.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">39.38</td>
    <td align="right">54.32</td>
    <td align="right">31.03</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">18.41</td>
    <td align="right">20.60</td>
    <td align="right">20.63</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">21.51</td>
    <td align="right">22.26</td>
    <td align="right">22.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">52.28</td>
    <td align="right">69.17</td>
    <td align="right">31.27</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">21.80</td>
    <td align="right">22.64</td>
    <td align="right">22.64</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">23.88</td>
    <td align="right">24.09</td>
    <td align="right">24.11</td>
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
    <td align="right">17.28</td>
    <td align="right">17.17</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.08</td>
    <td align="right">17.18</td>
    <td align="right">17.19</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.81</td>
    <td align="right">8.68</td>
    <td align="right">8.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.93</td>
    <td align="right">25.87</td>
    <td align="right">26.05</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.30</td>
    <td align="right">26.06</td>
    <td align="right">26.13</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.06</td>
    <td align="right">12.41</td>
    <td align="right">12.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.30</td>
    <td align="right">36.44</td>
    <td align="right">36.35</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.39</td>
    <td align="right">35.60</td>
    <td align="right">35.54</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.56</td>
    <td align="right">15.38</td>
    <td align="right">15.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.45</td>
    <td align="right">38.83</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.53</td>
    <td align="right">40.62</td>
    <td align="right">40.62</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">17.66</td>
    <td align="right">20.28</td>
    <td align="right">20.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4301</td>
    <td align="right">16.84</td>
    <td align="right">17.85</td>
    <td align="right">17.89</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">16.96</td>
    <td align="right">17.79</td>
    <td align="right">17.89</td>
    <td align="center">5</td>
    <td align="right">2.7323</td>
    <td align="right">7.95</td>
    <td align="right">8.73</td>
    <td align="right">8.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">22.76</td>
    <td align="right">26.35</td>
    <td align="right">26.35</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">25.35</td>
    <td align="right">25.91</td>
    <td align="right">25.91</td>
    <td align="center">8</td>
    <td align="right">0.5321</td>
    <td align="right">11.68</td>
    <td align="right">12.82</td>
    <td align="right">12.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">33.02</td>
    <td align="right">35.41</td>
    <td align="right">35.42</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">34.12</td>
    <td align="right">34.03</td>
    <td align="right">34.00</td>
    <td align="center">11</td>
    <td align="right">0.1189</td>
    <td align="right">14.34</td>
    <td align="right">16.28</td>
    <td align="right">16.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">37.44</td>
    <td align="right">38.06</td>
    <td align="right">38.09</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">42.45</td>
    <td align="right">41.23</td>
    <td align="right">40.99</td>
    <td align="center">13</td>
    <td align="right">0.0298</td>
    <td align="right">18.50</td>
    <td align="right">19.59</td>
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
    <td align="right">2.4627</td>
    <td align="right">7.45</td>
    <td align="right">8.75</td>
    <td align="right">8.64</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.30</td>
    <td align="right">17.18</td>
    <td align="right">17.18</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.08</td>
    <td align="right">17.20</td>
    <td align="right">17.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.97</td>
    <td align="right">12.19</td>
    <td align="right">12.19</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.94</td>
    <td align="right">25.87</td>
    <td align="right">26.06</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.24</td>
    <td align="right">26.07</td>
    <td align="right">26.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.98</td>
    <td align="right">15.21</td>
    <td align="right">15.21</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.29</td>
    <td align="right">36.44</td>
    <td align="right">36.36</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.38</td>
    <td align="right">35.59</td>
    <td align="right">35.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">17.54</td>
    <td align="right">19.08</td>
    <td align="right">19.07</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.42</td>
    <td align="right">38.80</td>
    <td align="right">38.81</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.62</td>
    <td align="right">40.55</td>
    <td align="right">40.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4960</td>
    <td align="right">7.68</td>
    <td align="right">8.48</td>
    <td align="right">8.49</td>
    <td align="center">5</td>
    <td align="right">2.4301</td>
    <td align="right">16.82</td>
    <td align="right">17.79</td>
    <td align="right">17.62</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">16.84</td>
    <td align="right">17.78</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4318</td>
    <td align="right">11.58</td>
    <td align="right">12.90</td>
    <td align="right">12.91</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">22.77</td>
    <td align="right">26.35</td>
    <td align="right">26.31</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">25.33</td>
    <td align="right">25.85</td>
    <td align="right">25.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0968</td>
    <td align="right">13.69</td>
    <td align="right">16.37</td>
    <td align="right">16.38</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">32.99</td>
    <td align="right">35.42</td>
    <td align="right">35.43</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">34.09</td>
    <td align="right">34.05</td>
    <td align="right">34.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">18.74</td>
    <td align="right">19.45</td>
    <td align="right">19.45</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">37.42</td>
    <td align="right">38.04</td>
    <td align="right">38.05</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">42.48</td>
    <td align="right">41.08</td>
    <td align="right">40.99</td>
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
    <td align="right">123.58</td>
    <td align="right">60.95</td>
    <td align="right">22.14</td>
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
    <td align="right">17.70</td>
    <td align="right">24.74</td>
    <td align="right">31.04</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.08</td>
    <td align="right">14.50</td>
    <td align="right">14.49</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">18.03</td>
    <td align="right">19.38</td>
    <td align="right">19.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">55.70</td>
    <td align="right">74.34</td>
    <td align="right">40.92</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">24.04</td>
    <td align="right">25.17</td>
    <td align="right">25.22</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">26.47</td>
    <td align="right">27.29</td>
    <td align="right">27.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">117.62</td>
    <td align="right">170.87</td>
    <td align="right">60.07</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.00</td>
    <td align="right">44.00</td>
    <td align="right">43.96</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">48.26</td>
    <td align="right">47.86</td>
    <td align="right">48.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">164.02</td>
    <td align="right">238.25</td>
    <td align="right">70.76</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">62.72</td>
    <td align="right">62.07</td>
    <td align="right">61.95</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">66.31</td>
    <td align="right">65.43</td>
    <td align="right">65.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1542</td>
    <td align="right">25.51</td>
    <td align="right">34.23</td>
    <td align="right">32.60</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">14.65</td>
    <td align="right">16.06</td>
    <td align="right">16.07</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.20</td>
    <td align="right">18.94</td>
    <td align="right">18.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">79.98</td>
    <td align="right">103.09</td>
    <td align="right">47.55</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">23.86</td>
    <td align="right">25.89</td>
    <td align="right">25.63</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">26.68</td>
    <td align="right">31.65</td>
    <td align="right">31.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">142.61</td>
    <td align="right">182.50</td>
    <td align="right">59.81</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">39.85</td>
    <td align="right">49.46</td>
    <td align="right">49.28</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">52.28</td>
    <td align="right">50.60</td>
    <td align="right">50.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">230.71</td>
    <td align="right">291.06</td>
    <td align="right">75.02</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">63.71</td>
    <td align="right">62.68</td>
    <td align="right">62.66</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">67.08</td>
    <td align="right">67.63</td>
    <td align="right">67.49</td>
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
    <td align="right">18.80</td>
    <td align="right">18.76</td>
    <td align="right">18.80</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.16</td>
    <td align="right">20.56</td>
    <td align="right">20.57</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">9.98</td>
    <td align="right">11.45</td>
    <td align="right">11.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">33.02</td>
    <td align="right">35.81</td>
    <td align="right">36.25</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.06</td>
    <td align="right">44.03</td>
    <td align="right">43.93</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">20.04</td>
    <td align="right">19.84</td>
    <td align="right">19.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.34</td>
    <td align="right">69.12</td>
    <td align="right">69.20</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">66.81</td>
    <td align="right">67.30</td>
    <td align="right">67.31</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">36.58</td>
    <td align="right">37.74</td>
    <td align="right">39.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">89.16</td>
    <td align="right">89.04</td>
    <td align="right">89.01</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.87</td>
    <td align="right">93.07</td>
    <td align="right">93.17</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">51.72</td>
    <td align="right">51.79</td>
    <td align="right">51.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4524</td>
    <td align="right">19.47</td>
    <td align="right">20.90</td>
    <td align="right">20.71</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">20.16</td>
    <td align="right">21.37</td>
    <td align="right">21.43</td>
    <td align="center">5</td>
    <td align="right">2.7367</td>
    <td align="right">9.99</td>
    <td align="right">10.97</td>
    <td align="right">10.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">37.39</td>
    <td align="right">42.79</td>
    <td align="right">42.87</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">37.16</td>
    <td align="right">35.91</td>
    <td align="right">35.70</td>
    <td align="center">8</td>
    <td align="right">0.5431</td>
    <td align="right">18.69</td>
    <td align="right">18.65</td>
    <td align="right">19.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">66.58</td>
    <td align="right">69.39</td>
    <td align="right">69.35</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">69.09</td>
    <td align="right">67.14</td>
    <td align="right">67.12</td>
    <td align="center">11</td>
    <td align="right">0.1181</td>
    <td align="right">39.57</td>
    <td align="right">39.64</td>
    <td align="right">39.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">86.99</td>
    <td align="right">87.67</td>
    <td align="right">87.70</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">95.72</td>
    <td align="right">93.22</td>
    <td align="right">92.87</td>
    <td align="center">13</td>
    <td align="right">0.0278</td>
    <td align="right">52.73</td>
    <td align="right">52.11</td>
    <td align="right">52.23</td>
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
    <td align="right">8.89</td>
    <td align="right">10.74</td>
    <td align="right">10.20</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">20.08</td>
    <td align="right">19.84</td>
    <td align="right">19.96</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">18.99</td>
    <td align="right">20.36</td>
    <td align="right">20.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">21.37</td>
    <td align="right">23.11</td>
    <td align="right">23.47</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.07</td>
    <td align="right">40.26</td>
    <td align="right">40.54</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">39.06</td>
    <td align="right">41.20</td>
    <td align="right">41.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">36.34</td>
    <td align="right">37.78</td>
    <td align="right">38.26</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.16</td>
    <td align="right">69.51</td>
    <td align="right">69.57</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">69.57</td>
    <td align="right">71.39</td>
    <td align="right">71.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.74</td>
    <td align="right">52.49</td>
    <td align="right">52.49</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.63</td>
    <td align="right">84.42</td>
    <td align="right">84.48</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.43</td>
    <td align="right">91.14</td>
    <td align="right">91.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4684</td>
    <td align="right">10.04</td>
    <td align="right">11.35</td>
    <td align="right">11.81</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.52</td>
    <td align="right">21.93</td>
    <td align="right">22.06</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">20.48</td>
    <td align="right">21.69</td>
    <td align="right">21.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4426</td>
    <td align="right">20.23</td>
    <td align="right">21.95</td>
    <td align="right">21.69</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">36.39</td>
    <td align="right">42.22</td>
    <td align="right">42.28</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">41.36</td>
    <td align="right">43.50</td>
    <td align="right">44.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0868</td>
    <td align="right">37.21</td>
    <td align="right">39.38</td>
    <td align="right">39.90</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">67.38</td>
    <td align="right">69.05</td>
    <td align="right">67.54</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">68.85</td>
    <td align="right">68.19</td>
    <td align="right">70.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">53.18</td>
    <td align="right">52.46</td>
    <td align="right">52.46</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">88.12</td>
    <td align="right">88.37</td>
    <td align="right">88.44</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">95.84</td>
    <td align="right">94.04</td>
    <td align="right">93.40</td>
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
    <td align="right">31.87</td>
    <td align="right">6.64</td>
    <td align="right">5.55</td>
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
    <td align="right">51.29</td>
    <td align="right">45.97</td>
    <td align="right">33.48</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.17</td>
    <td align="right">18.41</td>
    <td align="right">21.60</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.36</td>
    <td align="right">22.85</td>
    <td align="right">24.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">74.48</td>
    <td align="right">65.10</td>
    <td align="right">34.87</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">19.63</td>
    <td align="right">19.90</td>
    <td align="right">21.85</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.26</td>
    <td align="right">25.02</td>
    <td align="right">26.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">93.73</td>
    <td align="right">79.30</td>
    <td align="right">33.50</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">23.26</td>
    <td align="right">23.07</td>
    <td align="right">24.37</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.48</td>
    <td align="right">27.03</td>
    <td align="right">28.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">122.09</td>
    <td align="right">98.68</td>
    <td align="right">34.02</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">24.96</td>
    <td align="right">24.51</td>
    <td align="right">25.46</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.83</td>
    <td align="right">29.06</td>
    <td align="right">30.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1768</td>
    <td align="right">74.57</td>
    <td align="right">67.81</td>
    <td align="right">43.27</td>
    <td align="center">4</td>
    <td align="right">3.3657</td>
    <td align="right">21.91</td>
    <td align="right">22.42</td>
    <td align="right">24.41</td>
    <td align="center">5</td>
    <td align="right">3.0599</td>
    <td align="right">25.66</td>
    <td align="right">26.14</td>
    <td align="right">27.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3195</td>
    <td align="right">116.16</td>
    <td align="right">99.26</td>
    <td align="right">45.09</td>
    <td align="center">5</td>
    <td align="right">1.0452</td>
    <td align="right">23.19</td>
    <td align="right">23.43</td>
    <td align="right">24.50</td>
    <td align="center">6</td>
    <td align="right">0.8172</td>
    <td align="right">28.56</td>
    <td align="right">28.93</td>
    <td align="right">29.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0458</td>
    <td align="right">143.21</td>
    <td align="right">121.32</td>
    <td align="right">43.86</td>
    <td align="center">6</td>
    <td align="right">0.4017</td>
    <td align="right">26.55</td>
    <td align="right">26.44</td>
    <td align="right">27.04</td>
    <td align="center">7</td>
    <td align="right">0.2748</td>
    <td align="right">29.91</td>
    <td align="right">31.18</td>
    <td align="right">30.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0055</td>
    <td align="right">183.38</td>
    <td align="right">152.93</td>
    <td align="right">44.13</td>
    <td align="center">7</td>
    <td align="right">0.1892</td>
    <td align="right">29.52</td>
    <td align="right">27.85</td>
    <td align="right">28.21</td>
    <td align="center">8</td>
    <td align="right">0.1217</td>
    <td align="right">32.08</td>
    <td align="right">33.20</td>
    <td align="right">33.40</td>
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
    <td align="right">21.23</td>
    <td align="right">39.18</td>
    <td align="right">40.32</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.70</td>
    <td align="right">39.17</td>
    <td align="right">39.32</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.10</td>
    <td align="right">27.46</td>
    <td align="right">27.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.97</td>
    <td align="right">53.93</td>
    <td align="right">53.85</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">30.29</td>
    <td align="right">54.10</td>
    <td align="right">54.34</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.54</td>
    <td align="right">37.20</td>
    <td align="right">27.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">35.98</td>
    <td align="right">77.19</td>
    <td align="right">77.36</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.17</td>
    <td align="right">71.81</td>
    <td align="right">71.77</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">25.83</td>
    <td align="right">54.23</td>
    <td align="right">37.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.66</td>
    <td align="right">82.08</td>
    <td align="right">82.29</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">49.12</td>
    <td align="right">86.80</td>
    <td align="right">86.24</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">26.13</td>
    <td align="right">54.30</td>
    <td align="right">37.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4301</td>
    <td align="right">26.05</td>
    <td align="right">42.44</td>
    <td align="right">43.18</td>
    <td align="center">5</td>
    <td align="right">2.3209</td>
    <td align="right">27.48</td>
    <td align="right">42.80</td>
    <td align="right">43.17</td>
    <td align="center">5</td>
    <td align="right">2.7313</td>
    <td align="right">18.99</td>
    <td align="right">29.19</td>
    <td align="right">28.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4075</td>
    <td align="right">30.53</td>
    <td align="right">56.86</td>
    <td align="right">56.94</td>
    <td align="center">8</td>
    <td align="right">0.3787</td>
    <td align="right">33.16</td>
    <td align="right">57.61</td>
    <td align="right">57.62</td>
    <td align="center">8</td>
    <td align="right">0.5366</td>
    <td align="right">18.37</td>
    <td align="right">38.47</td>
    <td align="right">28.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0856</td>
    <td align="right">39.48</td>
    <td align="right">76.48</td>
    <td align="right">75.21</td>
    <td align="center">11</td>
    <td align="right">0.0603</td>
    <td align="right">42.84</td>
    <td align="right">84.22</td>
    <td align="right">75.23</td>
    <td align="center">11</td>
    <td align="right">0.1134</td>
    <td align="right">30.42</td>
    <td align="right">54.32</td>
    <td align="right">37.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0181</td>
    <td align="right">42.49</td>
    <td align="right">84.89</td>
    <td align="right">87.31</td>
    <td align="center">14</td>
    <td align="right">0.0124</td>
    <td align="right">48.49</td>
    <td align="right">92.09</td>
    <td align="right">91.61</td>
    <td align="center">13</td>
    <td align="right">0.0253</td>
    <td align="right">32.28</td>
    <td align="right">53.87</td>
    <td align="right">37.11</td>
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
    <td align="right">16.58</td>
    <td align="right">27.48</td>
    <td align="right">26.98</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.52</td>
    <td align="right">30.07</td>
    <td align="right">29.72</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">19.19</td>
    <td align="right">29.83</td>
    <td align="right">29.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">16.62</td>
    <td align="right">44.14</td>
    <td align="right">34.50</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">17.41</td>
    <td align="right">39.00</td>
    <td align="right">29.08</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">19.02</td>
    <td align="right">47.25</td>
    <td align="right">37.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">26.01</td>
    <td align="right">53.54</td>
    <td align="right">36.42</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">30.29</td>
    <td align="right">58.91</td>
    <td align="right">41.05</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">30.84</td>
    <td align="right">57.86</td>
    <td align="right">39.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">26.16</td>
    <td align="right">53.81</td>
    <td align="right">36.84</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">31.45</td>
    <td align="right">59.56</td>
    <td align="right">39.91</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">31.99</td>
    <td align="right">59.14</td>
    <td align="right">39.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4533</td>
    <td align="right">19.41</td>
    <td align="right">29.04</td>
    <td align="right">29.01</td>
    <td align="center">5</td>
    <td align="right">2.4471</td>
    <td align="right">21.40</td>
    <td align="right">31.72</td>
    <td align="right">31.72</td>
    <td align="center">5</td>
    <td align="right">2.3272</td>
    <td align="right">21.93</td>
    <td align="right">31.15</td>
    <td align="right">31.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4375</td>
    <td align="right">19.49</td>
    <td align="right">44.78</td>
    <td align="right">34.46</td>
    <td align="center">8</td>
    <td align="right">0.4137</td>
    <td align="right">20.26</td>
    <td align="right">39.74</td>
    <td align="right">30.06</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">22.44</td>
    <td align="right">47.28</td>
    <td align="right">37.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0906</td>
    <td align="right">30.47</td>
    <td align="right">53.62</td>
    <td align="right">36.49</td>
    <td align="center">11</td>
    <td align="right">0.0740</td>
    <td align="right">34.09</td>
    <td align="right">57.17</td>
    <td align="right">39.72</td>
    <td align="center">11</td>
    <td align="right">0.0604</td>
    <td align="right">35.07</td>
    <td align="right">58.10</td>
    <td align="right">39.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">31.78</td>
    <td align="right">53.75</td>
    <td align="right">36.90</td>
    <td align="center">13</td>
    <td align="right">0.0145</td>
    <td align="right">35.02</td>
    <td align="right">58.99</td>
    <td align="right">40.11</td>
    <td align="center">14</td>
    <td align="right">0.0129</td>
    <td align="right">35.98</td>
    <td align="right">78.70</td>
    <td align="right">59.95</td>
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
    <td align="right">61.68</td>
    <td align="right">33.29</td>
    <td align="right">18.27</td>
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
    <td align="right">55.47</td>
    <td align="right">48.15</td>
    <td align="right">35.19</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.82</td>
    <td align="right">18.78</td>
    <td align="right">22.48</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">24.46</td>
    <td align="right">32.33</td>
    <td align="right">33.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">105.03</td>
    <td align="right">110.65</td>
    <td align="right">47.05</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">22.74</td>
    <td align="right">21.97</td>
    <td align="right">23.75</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">30.69</td>
    <td align="right">28.13</td>
    <td align="right">29.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">219.90</td>
    <td align="right">196.61</td>
    <td align="right">60.63</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.82</td>
    <td align="right">38.25</td>
    <td align="right">39.56</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">46.76</td>
    <td align="right">46.12</td>
    <td align="right">47.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">346.61</td>
    <td align="right">291.70</td>
    <td align="right">72.16</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">42.83</td>
    <td align="right">42.59</td>
    <td align="right">43.71</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">58.69</td>
    <td align="right">58.80</td>
    <td align="right">60.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
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
    <td align="right">2.1542</td>
    <td align="right">80.98</td>
    <td align="right">94.53</td>
    <td align="right">53.70</td>
    <td align="center">4</td>
    <td align="right">3.3491</td>
    <td align="right">23.43</td>
    <td align="right">22.47</td>
    <td align="right">24.91</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.31</td>
    <td align="right">27.99</td>
    <td align="right">29.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">160.21</td>
    <td align="right">157.99</td>
    <td align="right">60.64</td>
    <td align="center">5</td>
    <td align="right">1.0294</td>
    <td align="right">26.73</td>
    <td align="right">31.04</td>
    <td align="right">32.24</td>
    <td align="center">6</td>
    <td align="right">0.8254</td>
    <td align="right">34.16</td>
    <td align="right">39.02</td>
    <td align="right">39.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0451</td>
    <td align="right">285.70</td>
    <td align="right">250.66</td>
    <td align="right">72.11</td>
    <td align="center">6</td>
    <td align="right">0.4029</td>
    <td align="right">44.83</td>
    <td align="right">45.11</td>
    <td align="right">45.33</td>
    <td align="center">7</td>
    <td align="right">0.2903</td>
    <td align="right">48.96</td>
    <td align="right">50.57</td>
    <td align="right">50.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">524.37</td>
    <td align="right">415.34</td>
    <td align="right">97.03</td>
    <td align="center">7</td>
    <td align="right">0.1877</td>
    <td align="right">46.49</td>
    <td align="right">47.83</td>
    <td align="right">47.52</td>
    <td align="center">8</td>
    <td align="right">0.1191</td>
    <td align="right">62.58</td>
    <td align="right">63.39</td>
    <td align="right">63.91</td>
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
    <td align="right">22.97</td>
    <td align="right">39.45</td>
    <td align="right">40.50</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">26.43</td>
    <td align="right">45.22</td>
    <td align="right">45.15</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.43</td>
    <td align="right">36.16</td>
    <td align="right">36.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.60</td>
    <td align="right">55.49</td>
    <td align="right">55.64</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">37.01</td>
    <td align="right">63.51</td>
    <td align="right">63.65</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">17.97</td>
    <td align="right">43.10</td>
    <td align="right">32.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">55.96</td>
    <td align="right">85.40</td>
    <td align="right">85.46</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">63.67</td>
    <td align="right">89.00</td>
    <td align="right">88.87</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">46.23</td>
    <td align="right">77.74</td>
    <td align="right">61.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">73.53</td>
    <td align="right">104.74</td>
    <td align="right">104.82</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">83.93</td>
    <td align="right">115.62</td>
    <td align="right">115.49</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.48</td>
    <td align="right">92.07</td>
    <td align="right">74.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
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
    <td align="right">2.4524</td>
    <td align="right">27.60</td>
    <td align="right">49.62</td>
    <td align="right">49.91</td>
    <td align="center">5</td>
    <td align="right">2.3116</td>
    <td align="right">30.27</td>
    <td align="right">43.08</td>
    <td align="right">43.55</td>
    <td align="center">5</td>
    <td align="right">2.7250</td>
    <td align="right">19.44</td>
    <td align="right">30.67</td>
    <td align="right">30.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4206</td>
    <td align="right">36.69</td>
    <td align="right">62.33</td>
    <td align="right">62.40</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">42.75</td>
    <td align="right">60.11</td>
    <td align="right">60.44</td>
    <td align="center">8</td>
    <td align="right">0.5385</td>
    <td align="right">26.15</td>
    <td align="right">45.14</td>
    <td align="right">35.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0786</td>
    <td align="right">66.66</td>
    <td align="right">95.13</td>
    <td align="right">94.00</td>
    <td align="center">11</td>
    <td align="right">0.0636</td>
    <td align="right">64.94</td>
    <td align="right">100.28</td>
    <td align="right">92.15</td>
    <td align="center">11</td>
    <td align="right">0.1183</td>
    <td align="right">53.82</td>
    <td align="right">77.75</td>
    <td align="right">62.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">76.32</td>
    <td align="right">107.14</td>
    <td align="right">108.85</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.64</td>
    <td align="right">119.89</td>
    <td align="right">119.80</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">66.88</td>
    <td align="right">90.22</td>
    <td align="right">75.04</td>
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
    <td align="right">17.24</td>
    <td align="right">29.14</td>
    <td align="right">29.06</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">24.58</td>
    <td align="right">60.28</td>
    <td align="right">60.22</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">19.74</td>
    <td align="right">30.98</td>
    <td align="right">31.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">18.67</td>
    <td align="right">56.20</td>
    <td align="right">47.04</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">20.22</td>
    <td align="right">41.31</td>
    <td align="right">30.93</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">35.77</td>
    <td align="right">66.54</td>
    <td align="right">57.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">47.38</td>
    <td align="right">77.55</td>
    <td align="right">61.84</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">51.42</td>
    <td align="right">82.03</td>
    <td align="right">63.96</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">52.58</td>
    <td align="right">81.58</td>
    <td align="right">63.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">59.21</td>
    <td align="right">91.59</td>
    <td align="right">75.76</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">61.18</td>
    <td align="right">96.58</td>
    <td align="right">77.78</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">64.47</td>
    <td align="right">99.11</td>
    <td align="right">79.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
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
    <td align="right">2.4644</td>
    <td align="right">21.76</td>
    <td align="right">30.48</td>
    <td align="right">30.44</td>
    <td align="center">5</td>
    <td align="right">2.4405</td>
    <td align="right">22.21</td>
    <td align="right">32.67</td>
    <td align="right">32.62</td>
    <td align="center">5</td>
    <td align="right">2.3265</td>
    <td align="right">22.19</td>
    <td align="right">32.55</td>
    <td align="right">32.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4413</td>
    <td align="right">21.77</td>
    <td align="right">56.36</td>
    <td align="right">46.21</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">22.82</td>
    <td align="right">41.73</td>
    <td align="right">31.76</td>
    <td align="center">8</td>
    <td align="right">0.3768</td>
    <td align="right">26.48</td>
    <td align="right">60.40</td>
    <td align="right">52.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0845</td>
    <td align="right">56.09</td>
    <td align="right">78.26</td>
    <td align="right">63.50</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">56.33</td>
    <td align="right">81.57</td>
    <td align="right">63.92</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">57.45</td>
    <td align="right">82.36</td>
    <td align="right">64.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">67.95</td>
    <td align="right">92.48</td>
    <td align="right">75.86</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">70.36</td>
    <td align="right">96.09</td>
    <td align="right">77.09</td>
    <td align="center">14</td>
    <td align="right">0.0116</td>
    <td align="right">79.36</td>
    <td align="right">104.78</td>
    <td align="right">85.39</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
